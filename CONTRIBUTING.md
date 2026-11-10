# Contributing

Thanks for helping. This list is generated, so the Markdown files are not edited by hand.

## How the repository is built

`data/metadata.jsonl` holds one prompt per line. `scripts/build.py` reads it and writes `README.md` and every file in `prompts/`. To rebuild:

```sh
python3 scripts/build.py --check-urls
```

The script needs Python 3 and nothing else. `--check-urls` requests every thumbnail and fails if one is missing.

## Report a problem

Open an issue if a prompt no longer gives a result close to its thumbnail, a link is broken, a credit is wrong or missing, or a prompt is yours and you want it credited differently or removed. Name the prompt and the model you ran it on.

## Suggest a prompt

Open an issue with:

- The prompt, exactly as you ran it.
- The model you ran it on and the aspect ratio.
- The result (attach the image, or link the clip).
- Where the prompt came from. If you wrote it, say so and confirm you are fine with CC BY 4.0. If you adapted it, give the author, the source link and its licence.

A prompt gets added once it has been run again on the named model and published with its result on [Prompt Generator](https://trypromptgenerator.com/prompts), because the thumbnails load from there. Prompts without a clear licence are not added.

## Pull requests

Pull requests are welcome for `scripts/build.py`, for wording fixes in `CONTRIBUTING.md`, and for corrections to a row in `data/metadata.jsonl` (a typo in a title, a wrong credit). Run the build and commit the regenerated files in the same pull request. Changes made only to `README.md` or `prompts/*.md` are overwritten by the next build.

## Style

- Plain, direct wording. No hype and no claims that are not in the data.
- Counts come from the data, never typed by hand.
- One paragraph per line in Markdown.
