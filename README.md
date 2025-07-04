✨ VISIOPATH — Intelligent Document & Visual Processing System

An AI-powered web app that enhances images, reconstructs text, and generates visuals from language — all in one platform.


⸻

🚀 Overview

VISIOPATH is a powerful multi-module AI application built with Flask, designed for real-world use cases in document enhancement and AI-based vision tasks.

🔍 It combines:
	•	🖼️ Image Enhancement (AI upscale)
	•	📄 Text Reconstruction (OCR + reconstruction)
	•	🎨 Text-to-Image Generation (prompt to image)

⸻

🧠 Features

🖼️ Image Enhancer

⚠️ Currently powered by Hugging Face API — ImgGen.ai temporarily unavailable

	•	Upload any low-resolution image (e.g., scanned document, old photo)
	•	Upscales image using ESRGAN AI model
	•	Clean before-after slider with instant download

📄 Text Reconstructor
	•	Upload scanned or noisy text image (handwritten or printed)
	•	Reconstructs and corrects missing or faded parts
	•	Downloads final output as .txt file

🎨 Text-to-Image Generator
	•	Input a natural language description
	•	Generates images via Together AI models
	•	Get shareable, high-quality visual content from simple text

⸻

🛠 Tech Stack

Layer	Tools Used
🎨 Frontend	HTML, CSS, JS (vanilla + slider effect)
🧠 Backend	Flask (Python)
🤖 AI APIs	Hugging Face, Together AI
🗂️ Others	dotenv, requests, Pillow


⸻

📁 Project Structure

visiopath/
├── app.py                  # Main Flask app with routing
├── .env                   # Environment vars (not tracked)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates for each module
├── static/                # CSS, images, JS
├── src/
│   ├── image_enhancer/    # ESRGAN logic, uploads, processed
│   ├── text_reconstructor/ # OCR & text rebuild logic
│   └── text_to_image/     # Together AI image generation


⸻

🔐 Environment Setup

Create a .env file in the root directory:

TOGETHER_API_KEY=your_together_ai_key
# IMGGEN_API_KEY=your_imggen_key (ImgGen.ai currently unavailable)
HF_TOKEN=your_huggingface_api_token

🔒 This file is private. It is ignored by Git.

⸻

💻 How to Run It Locally

1. Clone the repository

git clone https://github.com/yourusername/visiopath.git
cd visiopath

2. Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Add your .env file (see format above)

4. Run the app

python app.py

🚀 Visit http://localhost:5000 in your browser.

⸻

📸 Screenshots

Add module-wise screenshots below (optional):
	•	Image Enhancer with before-after slider ✅
	•	Text-to-Image preview result ✅
	•	Text Reconstructor UI ✅

⸻

🙌 Contributing

Pull requests welcome! Suggestions? Open an issue. 🛠️

⸻

⚖️ License

MIT — free to use, modify, and share.

⸻

🧠 Credits & Acknowledgements
	•	🤖 Replicate / ESRGAN
	•	🧬 Hugging Face
	•	🎨 Together AI
	•	💻 Flask

⸻

Crafted with 💜 by Om Badgujar
