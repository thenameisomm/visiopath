<p align="center">
  <img src="https://img.shields.io/badge/AI%20Toolkit-VISIOPATH-purple?style=for-the-badge&logo=python" alt="VISIOPATH Badge" />
</p>

<h1 align="center">✨ VISIOPATH</h1>
<p align="center"><i>Intelligent AI-Powered Platform for Image Enhancement, Text Reconstruction, and Text-to-Image Generation</i></p>

⸻

## 🚀 Overview

VISIOPATH is a modular AI web application built with Flask, integrating multiple intelligent features into a seamless and user-friendly experience:

- 🖼️ **AI-powered Image Enhancer**
- 📄 **Text Reconstructor** for noisy or partial text
- 🎨 **Text-to-Image Generator** for creative prompts

Whether you’re restoring photos, decoding faded documents, or bringing ideas to life through visuals — VISIOPATH is your all-in-one solution.

⸻

## 🧠 Features

### 🖼️ **Image Enhancer**

⚠️ *Currently powered by Hugging Face API — ImgGen.ai is temporarily unavailable*

- Enhance low-resolution or blurry images (e.g., scanned documents, old photos).
- Uses **Real-ESRGAN AI model** for sharp upscaling.
- Clean UI with a **before-after slider** + download option.

### 📄 **Text Reconstructor**

- Upload noisy, incomplete, or faded text images.
- Uses **deep learning models** to reconstruct missing characters.
- Result provided as a downloadable **.txt** file.

### 🎨 **Text-to-Image Generator**

- Generate stunning images from text prompts (e.g., “a sunset over a mountain temple”).
- Powered by **Together AI** text-to-image models.
- Great for storytelling, art, and education.

⸻

## 🛠 Tech Stack

| Layer             | Technologies                |
|-------------------|-----------------------------|
| 🎨 **Frontend**    | HTML, CSS, JavaScript       |
| ⚙️ **Backend**     | Python, Flask               |
| 🧠 **AI Models**   | Hugging Face, Together AI   |
| 🗂️ **Utilities**  | dotenv, requests, Pillow    |

⸻

## 📁 Project Structure

```bash
visiopath/
├── app.py                 → Main Flask application
├── .env                  → API keys and secrets (ignored by Git)
├── requirements.txt      → Python dependency list
├── static/               → Images, stylesheets, JavaScript
├── templates/            → HTML templates for all modules
├── src/                  → Main module code
│   ├── image_enhancer/   → AI-enhanced upscaler logic
│   │   ├── uploads/      → Uploaded images
│   │   ├── processed/    → Enhanced images
│   │   └── image_enhancer.py
│   ├── text_reconstructor/ → OCR + correction logic
│   │   ├── uploads/      → Input files
│   │   ├── processed/    → Output text files
│   │   └── text_reconstructor.py
│   └── text_to_image/    → Prompt-to-image generation logic
│       └── text_to_image.py

⸻

🔐 Environment Setup

Create a .env file in your root directory:

TOGETHER_API_KEY=your_together_ai_key
# IMGGEN_API_KEY=your_imggen_key (ImgGen.ai currently unavailable)
HF_TOKEN=your_huggingface_api_token

✅ Note: This file is ignored by Git (thanks to .gitignore).

⸻

💻 Getting Started
	1.	Clone the Repository

git clone https://github.com/thenameisomm/visiopath.git
cd visiopath

	2.	Create Virtual Environment

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

	3.	Install Dependencies

pip install -r requirements.txt

	4.	Add Your .env File

Add keys as shown above.
	5.	Run the App

python app.py

Visit http://localhost:5000 in your browser.

⸻

🤝 Contributing

Got suggestions, ideas, or improvements? Contributions are welcome!
	1.	Fork the repo
	2.	Create a new branch
	3.	Make your changes
	4.	Submit a pull request

⸻

⚖️ License

This project is licensed under the MIT License.

⸻

🙏 Acknowledgements
	•	🤖 Replicate / Real-ESRGAN
	•	🧬 Hugging Face
	•	🎨 Together AI
	•	💻 Flask

⸻

<p align="center">
  Made with ❤️ by <strong>Om Badgujar</strong>
</p>
```
