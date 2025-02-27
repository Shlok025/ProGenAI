# -*- coding: utf-8 -*-
"""gradio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bu1UNfn07uOigs4kx1YF0XjgNByGiYez
"""

!pip install -q gradio diffusers transformers accelerate
!pip install -q torch torchvision torchaudio

import gradio as gr
from diffusers import StableDiffusionXLPipeline
import torch
import gc
from IPython.display import clear_output

torch.cuda.empty_cache()
gc.collect()
clear_output()

# Professional prompt templates for each style
STYLE_PROMPTS = {
    'Anime': "masterpiece, best quality, anime style, highly detailed, vibrant colors, studio anime quality, {prompt}",
    'Sketch': "professional sketch, detailed linework, artistic drawing, high contrast, pencil drawing style, {prompt}",
    'Retro': "vintage aesthetic, retro design, classic style, old school vibe, nostalgic quality, {prompt}",
    'Funk': "psychedelic art, vibrant colors, funky design, groovy style, artistic expression, {prompt}",
    'Realistic': "photorealistic, highly detailed, professional photography, 8k uhd, clear focus, {prompt}"
}

# Negative prompts to improve quality
NEGATIVE_PROMPT = "blurry, low quality, distorted, deformed, ugly, bad anatomy, watermark, signature, poorly drawn, amateur"

def initialize_generator():
    """Initialize and configure the image generator with Colab-optimized settings"""
    # Check for GPU availability
    if not torch.cuda.is_available():
        print("WARNING: GPU not detected. This will run very slowly on CPU!")

    # Print available GPU memory
    if torch.cuda.is_available():
        print(f"Available GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")

    generator = StableDiffusionXLPipeline.from_pretrained(
        "segmind/SSD-1B",
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    )

    # Colab-specific optimizations
    generator.enable_attention_slicing()
    generator.enable_sequential_cpu_offload()  # Helps with Colab's limited memory

    # Set lower resolution for Colab
    generator.config.height = 512
    generator.config.width = 512

    return generator

def clear_memory():
    """Clear CUDA memory and garbage collection"""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()

def generate_image(prompt, category, num_inference_steps=30, guidance_scale=7.5):
    """Generate image with Colab-optimized memory handling"""
    try:
        # Clear memory before generation
        clear_memory()

        # Get base prompt template for selected category
        base_prompt = STYLE_PROMPTS.get(category, STYLE_PROMPTS['Realistic'])

        # Combine with user prompt
        enhanced_prompt = base_prompt.format(prompt=prompt)

        # Generate image with optimized parameters for Colab
        with torch.inference_mode():  # More memory efficient than no_grad
            result = generator(
                prompt=enhanced_prompt,
                negative_prompt=NEGATIVE_PROMPT,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
            )

        # Clear memory after generation
        clear_memory()

        return result.images[0]

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        clear_memory()  # Ensure memory is cleared even on error
        return None

def create_interface():
    """Create Gradio interface optimized for Colab"""
    categories = list(STYLE_PROMPTS.keys())

    interface = gr.Interface(
        fn=generate_image,
        inputs=[
            gr.Textbox(
                label="Enter Description",
                placeholder="Describe what you want to generate in detail",
                lines=3
            ),
            gr.Dropdown(
                choices=categories,
                label="Choose Style",
                value="Realistic"
            ),
            gr.Slider(
                minimum=20,
                maximum=50,
                value=30,
                step=1,
                label="Number of Inference Steps",
                info="Higher values = better quality but slower generation"
            ),
            gr.Slider(
                minimum=1.0,
                maximum=20.0,
                value=7.5,
                step=0.5,
                label="Guidance Scale",
                info="How closely to follow the prompt (higher = more literal)"
            )
        ],
        outputs=gr.Image(label="Generated Image"),
        title="Professional Text-to-Image Generator (Colab Version)",
        description="""
        Generate high-quality images from text descriptions using advanced AI.

        Prompt Tips:
        - Be specific in your descriptions
        - Include details about lighting, mood, and composition
        - Specify any particular artistic elements you want
        """,
        theme=gr.themes.Base()
    )
    return interface

# Third cell - Initialize generator and launch app
# Initialize the generator globally
print("Initializing generator... This may take a few moments.")
generator = initialize_generator()
print("Generator initialized successfully!")

# Launch the interface
app = create_interface()
app.launch(debug=True, share=True)