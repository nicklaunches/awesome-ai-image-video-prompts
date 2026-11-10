# AI product photo prompts

11 prompts with the result each one produced. Product shots for ads, listings and packaging. Copy a prompt with the button on its code block, then open its page on Prompt Generator for the full-size result, a breakdown of the prompt and variations.

Models used here: GPT Image 2 (2), Nano Banana Pro (2), Seedream 4.5 (2), FLUX.2 [pro] (1), Grok Imagine Image 2.0 (1), MAI Image 2.6 (1), Nano Banana 2 (1), Seedream 5.0 Lite (1).

[Back to all categories](../README.md) | [This category on Prompt Generator](https://trypromptgenerator.com/image-prompts/product-photos)

## Contents

- [3D product packaging box from a flat dieline](#3d-product-packaging-box-from-a-flat-dieline)
- [Beauty product close up with model applying pink lipstick](#beauty-product-close-up-with-model-applying-pink-lipstick)
- [Composite a product into a scene with realistic material relighting](#composite-a-product-into-a-scene-with-realistic-material-relighting)
- [Exploded view of a car with every part laid out in order](#exploded-view-of-a-car-with-every-part-laid-out-in-order)
- [Place a product into a character hand for UGC content](#place-a-product-into-a-character-hand-for-ugc-content)
- [Product mockup with custom design applied to object](#product-mockup-with-custom-design-applied-to-object)
- [Product technical analysis infographic for a shoe](#product-technical-analysis-infographic-for-a-shoe)
- [Professional fashion model wearing specific clothing items](#professional-fashion-model-wearing-specific-clothing-items)
- [Professional studio product photography of a white sneaker](#professional-studio-product-photography-of-a-white-sneaker)
- [Realistic 3D clothing mockup on a rotating human figure](#realistic-3d-clothing-mockup-on-a-rotating-human-figure)
- [Wine brand product collection mockup on wooden table](#wine-brand-product-collection-mockup-on-wooden-table)

## 3D product packaging box from a flat dieline

<a href="https://trypromptgenerator.com/p/3d-product-packaging-box-from-a-flat-dieline"><img src="https://trypromptgenerator.com/library/3d-product-packaging-box-from-a-flat-dieline.webp" width="220" alt="3D product packaging box from a flat dieline: result on Nano Banana Pro"></a>

**Model:** Nano Banana Pro | **Aspect ratio:** 1:1

```text
Assemble the dieline into a perfectly folded 3D box with accurate panel placement, clean edges, and undistorted typography. Preserve all artwork exactly as printed on the dieline. Render the box in a minimal, high-end studio setup on a soft neutral background with gentle diffused lighting, subtle shadows, and no extra props. Show the box upright in a refined ¾ angle. The box is prominent in frame.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-assemble_dieline.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/3d-product-packaging-box-from-a-flat-dieline)

## Beauty product close up with model applying pink lipstick

<a href="https://trypromptgenerator.com/p/beauty-product-close-up-with-model-applying-pink-lipstick"><img src="https://trypromptgenerator.com/library/beauty-product-close-up-with-model-applying-pink-lipstick.webp" width="220" alt="Beauty product close up with model applying pink lipstick: result on Grok Imagine Image 2.0"></a>

**Model:** Grok Imagine Image 2.0 | **Aspect ratio:** 9:16

```text
Create a vertical beauty product photography image. Use the first reference image as the character reference, keeping the young woman’s facial features, hairstyle, and cobalt blue textured outfit. Use the second reference image as the product reference, keeping the square pink matte lipstick.

Shoot in a close-up three-quarter side profile. The model does not face the camera directly. Show only her head, shoulders, neck, and one hand holding the lipstick. She raises the pink lipstick close to her lips and gently applies it, clearly showing the action of using the product.

The composition should focus tightly on her lips, the lipstick bullet, the lipstick tube, and her hand. The product and the lip application motion must be the most visible part of the image.

Use soft diffused studio daylight, a clean minimalist background, and a balanced color palette of cobalt blue and light pink. Use shallow depth of field. Keep the lipstick, lips, and hand in sharp focus, while the rest of the face and background fall into soft blur. The overall style should look like high-end commercial beauty product photography, realistic skin texture, soft shadows, and premium makeup advertising atmosphere.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_imagine_image_2_image_edit.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/beauty-product-close-up-with-model-applying-pink-lipstick)

## Composite a product into a scene with realistic material relighting

<a href="https://trypromptgenerator.com/p/composite-a-product-into-a-scene-with-realistic-material-relighting"><img src="https://trypromptgenerator.com/library/composite-a-product-into-a-scene-with-realistic-material-relighting.webp" width="220" alt="Composite a product into a scene with realistic material relighting: result on Seedream 4.5"></a>

**Model:** Seedream 4.5 | **Aspect ratio:** 1:1

```text
Task: Realistic Product Compositing with Material Preservation Goal: Insert the product from Input 2 into Input 1, ensuring placement is logical and lighting interacts accurately with the product's specific material properties.

Input Image(s):

Input 1 (Scene)
Input 2 (Product): {product_description}

Manual Material Breakdown (Critical): To ensure correct light interaction, treat the product as having the following physical properties:

Primary Material: [e.g., Matte Plastic / Brushed Aluminum / Clear Glass]

Reflectivity: [e.g., Low (dull reflections) / High (mirror-like)]

Texture: [e.g., Smooth / Grainy / Porous]

Reaction to Light: [e.g., "Should absorb light with soft highlights, no sharp glares"]

Secondary Material (if any): [e.g., Gold Foil Label / Glossy Cap]

Reaction to Light: [e.g., "Should catch sharp, bright specular highlights from the environment"]

Process:
Scene Analysis: Identify the logical ground plane/surface in Input 1.

Placement: Scale Input 2 uniformly (maintain aspect ratio) and place it on the surface.

Material-Based Relighting:

Do not simply overlay the scene colors onto the product.
Instead, map the environment light from Input 1 onto the contours of Input 2 based on the material definitions above.

Example: If the material is Matte, only the edge lighting and general ambient tone should change; do not add sharp reflections.

Example: If the material is Glossy, reflect the scene's details on the surface.

Shadows: Generate contact shadows that match the hardness/softness of shadows in the rest of the scene.

Technical Requirements:
Albedo Preservation: The intrinsic color of the product (e.g., "Brand Red") must not be washed out by the scene's lighting color.

Texture Fidelity: Do not smooth out surface details (grain, bumps) during the blending process.

Scaling: No non-uniform stretching.

Output: A composite where the lighting confirms the materiality of the product (e.g., makes the plastic look like plastic, not metal).
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-product_scene_relight.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/composite-a-product-into-a-scene-with-realistic-material-relighting)

## Exploded view of a car with every part laid out in order

<a href="https://trypromptgenerator.com/p/exploded-view-of-a-car-with-every-part-laid-out-in-order"><img src="https://trypromptgenerator.com/library/exploded-view-of-a-car-with-every-part-laid-out-in-order.webp" width="220" alt="Exploded view of a car with every part laid out in order: result on Nano Banana 2"></a>

**Model:** Nano Banana 2 | **Aspect ratio:** 1:1

```text
Slowly, its real physical components begin separating along natural assembly seams, transitioning into a clean, fully exploded view. Exterior casing, covers, buttons, ports, and internal structural parts separate in correct order and alignment, maintaining accurate scale and physical logic.

 No dialogue, no narration, no voiceover - only visual motion.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_eric_exploded_view.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/exploded-view-of-a-car-with-every-part-laid-out-in-order)

## Place a product into a character hand for UGC content

<a href="https://trypromptgenerator.com/p/place-a-product-into-a-character-hand-for-ugc-content"><img src="https://trypromptgenerator.com/library/place-a-product-into-a-character-hand-for-ugc-content.webp" width="220" alt="Place a product into a character hand for UGC content: result on Nano Banana Pro"></a>

**Model:** Nano Banana Pro | **Aspect ratio:** 1:1

```text
The subject from image 1 is holding the product from image 2, the product logo is visible.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-subject_holding_product.app.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/place-a-product-into-a-character-hand-for-ugc-content)

## Product mockup with custom design applied to object

<a href="https://trypromptgenerator.com/p/product-mockup-with-custom-design-applied-to-object"><img src="https://trypromptgenerator.com/library/product-mockup-with-custom-design-applied-to-object.webp" width="220" alt="Product mockup with custom design applied to object: result on FLUX.2 [pro]"></a>

**Model:** FLUX.2 [pro] | **Aspect ratio:** 1:1

```text
Apply the design from Reference Image 1 onto objects in Reference Image 2.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_fp8.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/product-mockup-with-custom-design-applied-to-object)

## Product technical analysis infographic for a shoe

<a href="https://trypromptgenerator.com/p/product-technical-analysis-infographic-for-a-shoe"><img src="https://trypromptgenerator.com/library/product-technical-analysis-infographic-for-a-shoe.webp" width="220" alt="Product technical analysis infographic for a shoe: result on GPT Image 2"></a>

**Model:** GPT Image 2 | **Aspect ratio:** 1:1

```text
Analyze the visual style, layout, color palette, and infographic format of the reference image. Create a product technical analysis infographic for shoe that perfectly matches the reference's design language, including layout structure, UI elements, feature callouts, and information presentation style.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_2_image_edit.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/product-technical-analysis-infographic-for-a-shoe)

## Professional fashion model wearing specific clothing items

<a href="https://trypromptgenerator.com/p/professional-fashion-model-wearing-specific-clothing-items"><img src="https://trypromptgenerator.com/library/professional-fashion-model-wearing-specific-clothing-items.webp" width="220" alt="Professional fashion model wearing specific clothing items: result on GPT Image 2"></a>

**Model:** GPT Image 2 | **Aspect ratio:** 1:1

```text
dress a professional female model with the provided clothing items. Crucially, preserve ALL original material properties, textures, and fabric characteristics exactly as shown in the source clothing images.

Model requirements:
- Professional fashion model with natural, confident pose
- Casual yet elegant stance suitable for contemporary streetwear
- Natural facial expression, looking slightly away from camera
- Modern hairstyle, effortless and stylish

Critical fabric and material preservation:
- Maintain EXACT fabric textures from the source images (fleece, denim, cotton, etc.)
- Preserve the fuzzy, fluffy texture of the grey hoodie exactly as shown
- Keep original fabric sheen, matte finish, or glossiness unchanged
- Retain precise color values, saturation, and undertones of all garments
- Preserve fabric weight appearance (heavy fleece vs. light cotton)
- Maintain weave patterns, knit structures, and material densities
- Keep all surface details: pile height, fabric grain, textile characteristics
- Preserve stitching details, seam types, and construction elements

Clothing fit and draping:
- Fit the provided clothing naturally to the model's body while maintaining fabric properties
- Natural fabric behavior based on original material type (stiff denim vs. soft fleece)
- Realistic folds, wrinkles, and creases appropriate to each fabric type
- Proper layering with each garment's original thickness and volume
- Accurate shadows and highlights respecting original material reflectance

Technical requirements:
- Match lighting interaction with each fabric type from source images
- Preserve fabric subsurface scattering (especially for fleece/fuzzy materials)
- Maintain original color temperature and saturation of all garments
- Keep exact contrast levels between different fabric areas
- Professional fashion photography lighting showcasing material details
- Clean neutral background (white or light grey)
- High-resolution, editorial quality with sharp fabric texture detail
- Photorealistic rendering with microscopic attention to textile authenticity

Environment:
- Lighting should reveal fabric textures clearly
- Color-neutral lighting to preserve original garment colors
- Studio-quality illumination showing material properties accurately

Do not alter, enhance, or "improve" the fabric appearances. Transfer the exact material characteristics from the source clothing images to the dressed model. Preserve all design elements, logos, graphics, and details exactly as shown. No watermarks or additional text.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_fashion_billboard_generator.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/professional-fashion-model-wearing-specific-clothing-items)

## Professional studio product photography of a white sneaker

<a href="https://trypromptgenerator.com/p/professional-studio-product-photography-of-a-white-sneaker"><img src="https://trypromptgenerator.com/library/professional-studio-product-photography-of-a-white-sneaker.webp" width="220" alt="Professional studio product photography of a white sneaker: result on Seedream 4.5"></a>

**Model:** Seedream 4.5 | **Aspect ratio:** 1:1

```text
Professional studio product photography of a pristine white Adidas Samba sneaker from image 1, positioned at a dynamic three-quarter angle. The lighting is dramatic and cool-toned, featuring a hard spotlight that creates a glowing halo effect on the ground while casting soft shadows. The background is a seamless, clean gradient transitioning from a light silver-gray top to a deep anthracite black floor. Minimal composition with generous negative space, shot with shallow depth of field (f/2.8) to emphasize product details while softly blurring the background.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-photo_to_product_vid.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/professional-studio-product-photography-of-a-white-sneaker)

## Realistic 3D clothing mockup on a rotating human figure

<a href="https://trypromptgenerator.com/p/realistic-3d-clothing-mockup-on-a-rotating-human-figure"><img src="https://trypromptgenerator.com/library/realistic-3d-clothing-mockup-on-a-rotating-human-figure.webp" width="220" alt="Realistic 3D clothing mockup on a rotating human figure: result on MAI Image 2.6"></a>

**Model:** MAI Image 2.6 | **Aspect ratio:** 1:1

```text
The clothing presents a realistic 3D effect as if worn on a human figure, rotating slightly to the left, with a white background.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_mai_image_26_flash_image_edit.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/realistic-3d-clothing-mockup-on-a-rotating-human-figure)

## Wine brand product collection mockup on wooden table

<a href="https://trypromptgenerator.com/p/wine-brand-product-collection-mockup-on-wooden-table"><img src="https://trypromptgenerator.com/library/wine-brand-product-collection-mockup-on-wooden-table.webp" width="220" alt="Wine brand product collection mockup on wooden table: result on Seedream 5.0 Lite"></a>

**Model:** Seedream 5.0 Lite | **Aspect ratio:** 1:1

```text
Photorealistic commercial product photography, a complete wine brand collection display derived from the reference image. Central hero is the original wine bottle with its purple label and two-women flat grain illustration. Surrounding products include a rigid wine gift box, canvas tote bag, wine glass, corkscrew, wooden cork, small grape cluster, branded paper card and fabric pouch. All items are printed or decorated with the same brand visual identity from reference: two women characters, geometric flowers, lavender purple, royal blue, pink, orange, grainy flat graphic style. Arranged on a light wooden table with soft studio lighting, elegant lifestyle mockup, shallow depth of field, realistic glass, paper and fabric texture, premium wine brand styling, clean background, high detail.
```

Credit: prompt adapted from [ComfyUI templates](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_0_flash_image_edit.json) by Comfy Org, MIT licence.

[Result, breakdown and variations →](https://trypromptgenerator.com/p/wine-brand-product-collection-mockup-on-wooden-table)
