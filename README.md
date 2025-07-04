✨ VISIOPATH — Intelligent Document & Visual Processing System

An AI-powered web app that enhances images, reconstructs text, and generates visuals from language — all in one platform.


⸻

🚀 Overview

VISIOPATH is a powerful multi-module AI application built with Flask, designed for real-world use cases in document enhancement and AI-based vision tasks. It seamlessly combines three intelligent features — Image Enhancement, Text Reconstruction, and Text-to-Image Generation — into a single intuitive web platform. Whether you’re restoring photos, decoding damaged documents, or generating art from prompts, VISIOPATH delivers high-quality results backed by AI APIs.

<hr/>


🧠 Features

🖼️ Image Enhancer

⚠️ Currently powered by Hugging Face API — ImgGen.ai temporarily unavailable

	•	Enhance low-resolution or blurry images (e.g., scanned documents, old photos).
	•	Uses ESRGAN AI model for high-quality upscaling.
	•	Clean UI with before-after image slider and instant download.

📄 Text Reconstructor
	•	Upload scanned or degraded images containing text.
	•	Reconstructs and completes partial or faded content.
	•	Outputs a clean .txt file with the corrected and recovered text.

🎨 Text-to-Image Generator
	•	Convert text prompts (e.g., “A castle on the moon”) into vivid AI-generated images.
	•	Powered by Together AI’s image generation models.
	•	Supports multiple use cases: creative, commercial, or fun.

<hr/>


🛠 Tech Stack

Layer	Tools Used
🎨 Frontend	HTML, CSS, JavaScript
🧠 Backend	Python, Flask
🤖 AI APIs	Hugging Face, Together AI
🗂️ Utility	dotenv, requests, Pillow

<hr/>


📁 Project Structure

visiopath/
├── app.py                 # Main Flask application
├── .env                   # Environment variables (not pushed to GitHub)
├── requirements.txt       # Python dependency list
├── templates/             # HTML templates for rendering modules
├── static/                # CSS, JS, image assets
├── src/
│   ├── image_enhancer/    # Image enhancer logic + uploads folder
│   ├── text_reconstructor/ # Text OCR and fixer
│   └── text_to_image/     # Prompt-to-image generator

<hr/>


🔐 Environment Setup

Create a .env file in the root project directory with the following keys:

TOGETHER_API_KEY=your_together_ai_key_here
# IMGGEN_API_KEY=your_imggen_key_here (ImgGen.ai currently unavailable)
HF_TOKEN=your_huggingface_api_token_here

🔒 .env is secured using .gitignore and never pushed to GitHub.

<hr/>


💻 How to Run Locally

1. Clone the repository

git clone https://github.com/yourusername/visiopath.git
cd visiopath

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install the dependencies

pip install -r requirements.txt

4. Add your API keys to .env file (as shown above)

5. Start the Flask app

python app.py

Then open your browser and visit:

http://localhost:5000

<hr/>


📸 Screenshots (Optional)

Add visual examples for each module below:
	•	✅ Image Enhancer UI with before-after result
	•	✅ Text-to-Image module with generated artwork
	•	✅ Text Reconstructor showing input/output example

<hr/>


🙌 Contributing

Have suggestions, improvements, or ideas? Fork the repo and open a pull request. Collaboration is welcome!

<hr/>


⚖️ License

MIT License — you’re free to use, modify, and distribute this project.

<hr/>


🧠 Acknowledgements
	•	🤖 Replicate / Real-ESRGAN
	•	🧬 Hugging Face
	•	🎨 Together AI
	•	💻 Flask

<hr/>


Made with 💜 by Om Badgujar
