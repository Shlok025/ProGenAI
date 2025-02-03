# ProGenAI

## Overview

*ProGenAI* is an interactive Gradio-based app that transforms text descriptions into high-quality images. Leveraging state-of-the-art AI models like Stable Diffusion, it offers a versatile platform for generating artwork in multiple styles, from photorealistic to anime. The app is optimized for smooth performance even in resource-limited environments like Google Colab.

## Features

### Key Features
- *Multi-Style Image Generation*: Choose from styles like Anime, Sketch, Retro, Funk, and Realistic.
- *Optimized for Performance*: Enhanced memory management for seamless generation in environments like Google Colab.
- *Professional Quality*: Generates high-resolution, detailed images using advanced AI pipelines.
- *User-Friendly Interface*: Intuitive and modern interface powered by Gradio for easy interaction.

### Visualizations and UI Components
1. *Main Header*: Displays the application title and a brief description.
2. *Prompt Input*: Users can enter detailed text descriptions for image generation.
3. *Style Selection*: Dropdown menu for selecting the desired artistic style.
4. *Advanced Controls*: Sliders for adjusting inference steps and guidance scale for quality control.

### Interactive Filters
- *Style Selection*: Pick from various artistic styles to customize your image.
- *Inference Steps*: Adjust the number of steps to control image quality and generation speed.
- *Guidance Scale*: Fine-tune how closely the AI adheres to the prompt.

## Requirements

To run this app, ensure the following:

1. *Gradio*: Install Gradio for building the interactive interface.
2. *Diffusers & Transformers*: Libraries for AI model integration.
3. *Torch*: Required for deep learning and model execution.
4. *Python Environment*: Ensure Python 3.9 or higher is installed.

Install the dependencies using:

```bash
pip install gradio diffusers transformers accelerate torch torchvision torchaudio
```

## Setup Instructions

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Shlok025/ProGenAI.git
cd ProGenAI
```

2. Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Gradio app:

```bash
python gradio.py
```

## Usage

1. Launch the app and enter a detailed description of the image you want to generate.
2. Choose your desired style from the dropdown menu.
3. Adjust the inference steps and guidance scale sliders as needed.
4. Click *Generate* to create your image.
5. Download or refine the generated image as desired.

## Images

### Home:
![Home](https://github.com/user-attachments/assets/7bf6eb47-7c22-4d0b-a3cb-466945ee3e15)

### Generated Images:
![Generated Image 1](https://github.com/user-attachments/assets/b59335d4-9e97-431a-b862-8d6d31e0fe05)

![Generated Image 2](https://github.com/user-attachments/assets/22d81718-2120-4bbc-aad1-942394a3574a)

![Generated Image 3](https://github.com/user-attachments/assets/cb2eb25f-6b2f-4498-911b-9bc7898f46be)


## Contribution

Contributions are welcome! If you have suggestions for improvements or encounter issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Footer

Developed with ❤ by [Shlok Gaikwad](https://github.com/Shlok025/)

⚡ Features: Multi-Style Image Generation, AI-Powered Art, and Professional Quality Output

