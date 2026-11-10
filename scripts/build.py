#!/usr/bin/env python3
"""Rebuild README.md and prompts/*.md from data/metadata.jsonl.

Usage: python3 scripts/build.py [--metadata PATH] [--out DIR] [--check-urls]

Standard library only. Thumbnails are not stored here: they load from
trypromptgenerator.com. --check-urls requests every thumbnail and fails
if one does not return 200 with an image content type.
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITE = "https://trypromptgenerator.com"
SITE_NAME = "Prompt Generator"
OWN_SOURCE = "trypromptgenerator.com"
README_PICKS = 4
THUMB_WIDTH = 220
LINK_TEXT = "Result, breakdown and variations →"

# slug in the data -> (file name, heading, site hub path, one-line intro)
CATEGORIES = [
    (
        "gemini-photo",
        "gemini-ai-photo-prompts",
        "Gemini AI photo prompts (Nano Banana)",
        "/image-prompts/gemini-photo",
        "Upload your own photo to Gemini, paste the prompt, and get a new scene with the same face.",
    ),
    (
        "photo-editing",
        "ai-photo-editing-prompts",
        "AI photo editing prompts",
        "/image-prompts/photo-editing",
        "Edits to a photo you already have: restyle, relight, restore, swap a background, change an outfit.",
    ),
    (
        "couple",
        "couple-photo-prompts",
        "Couple photo prompts for Gemini",
        "/image-prompts/couple",
        "Two-person photo prompts that keep both faces from the photos you upload.",
    ),
    (
        "christmas",
        "christmas-photo-prompts",
        "Christmas photo prompts",
        "/image-prompts/christmas",
        "Holiday portraits, cards and family scenes made from your own photo.",
    ),
    (
        "3d-figurine",
        "3d-figurine-prompts",
        "3D figurine prompts",
        "/image-prompts/3d-figurine",
        "Figurines, toys, collectibles and character sheets.",
    ),
    (
        "product-photos",
        "product-photo-prompts",
        "AI product photo prompts",
        "/image-prompts/product-photos",
        "Product shots for ads, listings and packaging.",
    ),
    (
        "ai-art",
        "ai-art-prompts",
        "AI art and image prompts (FLUX, Qwen Image, Recraft)",
        "/image-prompts/ai-art",
        "Text-to-image prompts: illustration, posters, characters, photoreal scenes.",
    ),
    (
        "cinematic",
        "cinematic-video-prompts",
        "Cinematic AI video prompts (Seedance, Veo, Wan)",
        "/video-prompts/cinematic",
        "Shot-by-shot video prompts with camera moves, light and sound.",
    ),
    (
        "product-video",
        "product-video-prompts",
        "Product video prompts",
        "/video-prompts/product-video",
        "Short product clips for ads and store pages.",
    ),
    (
        "social-video",
        "social-video-prompts",
        "Social video prompts for Reels, TikTok and Shorts",
        "/video-prompts/social-video",
        "Vertical clips made for short-form feeds.",
    ),
    (
        "nature",
        "nature-video-prompts",
        "Nature video prompts",
        "/video-prompts/nature",
        "Landscapes, weather and wildlife for b-roll.",
    ),
]

MODEL_NAMES = {
    "flux-2-klein": "FLUX.2 [klein] 4B",
    "flux-2-pro": "FLUX.2 [pro]",
    "flux-3-image": "FLUX.3 Image",
    "flux-3-video": "FLUX.3 Video",
    "gemini-omni-1-2-flash": "Gemini Omni 1.2 Flash",
    "gpt-image-1-mini": "GPT Image 1 Mini",
    "gpt-image-2": "GPT Image 2",
    "gpt-image-2-5-flare": "GPT Image 2.5 Flare",
    "grok-imagine-image": "Grok Imagine Image 2.0",
    "grok-imagine-video-1-5": "Grok Imagine Video 1.5",
    "hailuo-2-3": "MiniMax Hailuo 2.3",
    "kling-3-pro": "Kling 3.0 Pro",
    "kling-o1": "Kling Video O1",
    "mai-image-2-6": "MAI Image 2.6",
    "nano-banana": "Nano Banana",
    "nano-banana-2": "Nano Banana 2",
    "nano-banana-pro": "Nano Banana Pro",
    "qwen-image-3": "Qwen Image 3",
    "recraft-v4-1": "Recraft V4.1",
    "seedance-2": "Seedance 2.0",
    "seedance-2-5": "Seedance 2.5",
    "seedream-4-5": "Seedream 4.5",
    "seedream-5-lite": "Seedream 5.0 Lite",
    "seedream-5-pro": "Seedream 5.0 Pro",
    "veo-3-1": "Veo 3.1",
    "wan-2-7": "Wan 2.7",
    "wan-3": "Wan 3.0",
    "z-image-turbo": "Z-Image Turbo",
}

LICENSE_NAMES = {"MIT": "MIT", "Apache-2.0": "Apache 2.0", "CC0-1.0": "CC0 1.0", "CC-BY-4.0": "CC BY 4.0"}

BANNED = (chr(0x2014), "no" + "-fluff")


def model_name(slug):
    return MODEL_NAMES.get(slug, slug.replace("-", " ").title())


def thumb_url(row):
    folder = "library/video" if row["kind"] == "video" else "library"
    return f"{SITE}/{folder}/{row['slug']}.webp"


def is_own(row):
    return row["prompt_source"] == OWN_SOURCE


def fence_for(text):
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def md_text(text):
    return re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text)


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def entry(row, level):
    title = row["title"].strip()
    alt = html.escape(f"{title}: {'poster frame' if row['kind'] == 'video' else 'result'} on {model_name(row['model'])}", quote=True)
    meta = [f"**Model:** {model_name(row['model'])}"]
    if row.get("aspect_ratio") and row["aspect_ratio"] != "original":
        meta.append(f"**Aspect ratio:** {row['aspect_ratio']}")
    if row["kind"] == "video":
        meta.append("**Video prompt:** the thumbnail is the poster frame, the clip plays on the page")
    prompt = row["prompt"].strip("\n")
    fence = fence_for(prompt)
    lines = [
        f"{'#' * level} {md_text(title)}",
        "",
        f'<a href="{row["page_url"]}"><img src="{thumb_url(row)}" width="{THUMB_WIDTH}" alt="{alt}"></a>',
        "",
        " | ".join(meta),
        "",
        f"{fence}text",
        prompt,
        fence,
        "",
    ]
    if not is_own(row):
        licence = LICENSE_NAMES.get(row["prompt_source_license"], row["prompt_source_license"])
        lines += [
            f"Credit: prompt adapted from [{md_text(row['prompt_source'])}]({row['prompt_source_url']}) by {md_text(row['prompt_source_author'])}, {licence} licence.",
            "",
        ]
    lines += [f"[{LINK_TEXT}]({row['page_url']})", ""]
    return "\n".join(lines)


def sort_rows(rows):
    return sorted(rows, key=lambda r: (not is_own(r), r["title"].lower()))


def pick(cat_rows, shown):
    """README picks: not shown in an earlier category, one per model first, the site's own prompts first."""
    fresh = [r for r in cat_rows if r["slug"] not in shown] or cat_rows
    picks, models = [], set()
    for r in fresh:
        if r["model"] not in models:
            picks.append(r)
            models.add(r["model"])
    picks += [r for r in fresh if r not in picks]
    picks = sort_rows(picks[:README_PICKS])
    shown.update(r["slug"] for r in picks)
    return picks


def models_line(rows):
    counts = Counter(model_name(r["model"]) for r in rows)
    return ", ".join(f"{name} ({n})" for name, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def category_page(cat, rows):
    slug, fname, heading, hub, intro = cat
    out = [
        f"# {heading}",
        "",
        f"{plural(len(rows), 'prompt')} with the result each one produced. {intro} Copy a prompt with the button on its code block, then open its page on {SITE_NAME} for the full-size result, a breakdown of the prompt and variations.",
        "",
        f"Models used here: {models_line(rows)}.",
        "",
        f"[Back to all categories](../README.md) | [This category on {SITE_NAME}]({SITE}{hub})",
        "",
        "## Contents",
        "",
    ]
    seen = Counter()
    for r in rows:
        out.append(f"- [{md_text(r['title'].strip())}](#{anchor(r['title'].strip(), seen)})")
    out.append("")
    for r in rows:
        out.append(entry(r, 2))
    return "\n".join(out).rstrip("\n") + "\n"


def anchor(title, seen):
    base = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
    n = seen[base]
    seen[base] += 1
    return base if n == 0 else f"{base}-{n}"


def readme(rows, by_cat):
    images = sum(r["kind"] == "image" for r in rows)
    videos = len(rows) - images
    own = sum(is_own(r) for r in rows)
    model_counts = Counter(r["model"] for r in rows)
    out = [
        "# Awesome AI Image and Video Prompts",
        "",
        f"{len(rows)} tested AI image and video prompts across {len(model_counts)} models, including Nano Banana Pro (the model behind Gemini AI photo prompts), FLUX.2, Qwen Image, Seedance 2.0 and Veo 3.1: {images} image prompts and {videos} video prompts, each shown with the result it produced on the named model.",
        "",
        f"The prompts come from the [{SITE_NAME} prompt library]({SITE}/prompts). Every entry has a copy button on its code block and a link to its page, where you get the full-size result (or the playable clip), a breakdown of what each part of the prompt does, and variations to try.",
        "",
        "## Contents",
        "",
        "| Category | Kind | Prompts |",
        "|---|---|---|",
    ]
    for cat in CATEGORIES:
        slug, fname, heading, hub, intro = cat
        kind = by_cat[slug][0]["kind"].capitalize()
        out.append(f"| [{heading}](prompts/{fname}.md) | {kind} | {len(by_cat[slug])} |")
    out += [
        "",
        f"A prompt can sit in more than one category, so the rows add up to more than {len(rows)}.",
        "",
        "Also on this page: [How to use a prompt](#how-to-use-a-prompt) | [Prompts by model](#prompts-by-model) | [Write your own prompt](#write-your-own-prompt) | [Licence and credits](#licence-and-credits)",
        "",
        "## How to use a prompt",
        "",
        "1. Find a result you like and press the copy button on the code block under it.",
        "2. Paste the prompt into the model named on the entry. For Gemini AI photo prompts and photo editing prompts, upload your own photo first, then paste.",
        "3. Change the details (subject, clothes, place, light) to fit your picture. The entry's page lists variations to try.",
        "",
        "Results differ between models. A prompt written for Nano Banana Pro will run on other image models, but the look will change.",
        "",
    ]
    shown = set()
    for cat in CATEGORIES:
        slug, fname, heading, hub, intro = cat
        cat_rows = by_cat[slug]
        picks = pick(cat_rows, shown)
        out += [
            f"## {heading}",
            "",
            f"{intro} {plural(len(cat_rows), 'prompt')} in this category, {len(picks)} shown here. [See all {len(cat_rows)}](prompts/{fname}.md).",
            "",
        ]
        for r in picks:
            out.append(entry(r, 3))
        if len(cat_rows) > len(picks):
            out += [f"[See all {len(cat_rows)} in this category →](prompts/{fname}.md)", ""]
    out += [
        "## Prompts by model",
        "",
        "| Model | Kind | Prompts |",
        "|---|---|---|",
    ]
    kind_of = {r["model"]: r["kind"] for r in rows}
    for m, n in sorted(model_counts.items(), key=lambda kv: (-kv[1], model_name(kv[0]))):
        out.append(f"| {md_text(model_name(m))} | {kind_of[m].capitalize()} | {n} |")
    out += [
        "",
        "## Write your own prompt",
        "",
        f"- [Image prompt generator]({SITE}/image-prompt-generator): describe the picture, pick the model, get a prompt in that model's syntax.",
        f"- [Video prompt generator]({SITE}/video-prompt-generator): the same for Veo, Seedance and other video models.",
        f"- [Image to prompt]({SITE}/image-to-prompt): upload a picture and get the prompt that describes it.",
        f"- [The full prompt library]({SITE}/prompts): more image and video prompts, plus text and website prompts.",
        "",
        "## Licence and credits",
        "",
        f"- {own} prompts were written by {SITE_NAME}. Their text and titles are under [CC BY 4.0](LICENSE): credit \"{SITE_NAME} ({OWN_SOURCE})\" with a link.",
    ]
    third = Counter((r["prompt_source"], r["prompt_source_author"], r["prompt_source_license"]) for r in rows if not is_own(r))
    for (src, author, lic), n in sorted(third.items(), key=lambda kv: -kv[1]):
        out.append(f"- {plural(n, 'prompt')} adapted from {md_text(src)} ({md_text(author)}) {'keep' if n != 1 else 'keeps'} the original {LICENSE_NAMES.get(lic, lic)} licence. Each entry carries its own credit line with the source link.")
    out += [
        "- Prompts whose original licence could not be confirmed were left out.",
        "- Thumbnails load from trypromptgenerator.com and are not part of this repository.",
        "",
        "Want to add a prompt or fix one? See [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
    ]
    return "\n".join(out)


def check_urls(rows):
    def probe(row):
        url = thumb_url(row)
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "prompt-list-build"})
            with urllib.request.urlopen(req, timeout=30) as res:
                ok = res.status == 200 and res.headers.get("Content-Type", "").startswith("image/")
                return url, ok, f"{res.status} {res.headers.get('Content-Type')}"
        except Exception as err:
            return url, False, str(err)

    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(probe, rows))
    bad = [r for r in results if not r[1]]
    print(f"thumbnails: {len(results) - len(bad)} of {len(results)} passed")
    for url, _, why in bad:
        print(f"  FAIL {url} ({why})")
    return not bad


def main():
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser()
    ap.add_argument("--metadata", default=str(root / "data" / "metadata.jsonl"))
    ap.add_argument("--out", default=str(root))
    ap.add_argument("--check-urls", action="store_true")
    args = ap.parse_args()

    rows = [json.loads(line) for line in Path(args.metadata).read_text(encoding="utf-8").splitlines() if line.strip()]
    known = {c[0] for c in CATEGORIES}
    unknown = sorted({c for r in rows for c in r["categories"]} - known)
    if unknown:
        sys.exit(f"categories without a heading in CATEGORIES: {unknown}")
    if any(not r["page_url"].startswith(f"{SITE}/p/") for r in rows):
        sys.exit("a row has a page_url outside the site")

    by_cat = {c[0]: sort_rows([r for r in rows if c[0] in r["categories"]]) for c in CATEGORIES}
    out = Path(args.out)
    (out / "prompts").mkdir(parents=True, exist_ok=True)
    files = {out / "README.md": readme(rows, by_cat)}
    for cat in CATEGORIES:
        if by_cat[cat[0]]:
            files[out / "prompts" / f"{cat[1]}.md"] = category_page(cat, by_cat[cat[0]])
    for old in (out / "prompts").glob("*.md"):
        if old not in files:
            old.unlink()
    for path, text in files.items():
        for bad in BANNED:
            if bad in text.lower():
                sys.exit(f"{path.name} contains a banned string: {bad!r}")
        path.write_text(text, encoding="utf-8")
        print(f"{path.relative_to(out)}: {len(text.encode('utf-8')):,} bytes")
    print(f"{len(rows)} prompts, " + ", ".join(f"{c[0]} {len(by_cat[c[0]])}" for c in CATEGORIES))
    if args.check_urls and not check_urls(rows):
        sys.exit(1)


if __name__ == "__main__":
    main()
