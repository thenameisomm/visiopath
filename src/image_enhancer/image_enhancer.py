import os
import requests
import base64
from flask import request, jsonify, send_from_directory
from dotenv import load_dotenv

# ✅ Load API Key
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv(env_path)

API_KEY = os.getenv("IMGGEN_API_KEY")

# ✅ Debug: Print API Key
print("🔑 API Key Loaded:", API_KEY)

if not API_KEY:
    print("❌ ERROR: API Key missing. Check .env file!")
    exit()

# ✅ Define API Endpoint for Upscaling
IMGGEN_UPSCALE_URL = "https://app.imggen.ai/v1/upscale-image"

# ✅ Define Upload & Download Folders
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
PROCESSED_FOLDER = os.path.join(os.path.dirname(__file__), 'processed')  # ✅ New folder for processed images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# ✅ Process Image Enhancement & Enable Download
def process_image_enhancement():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # ✅ Save Uploaded File
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # ✅ Send Image to ImgGen API
    with open(file_path, "rb") as image_file:
        response = requests.post(
            IMGGEN_UPSCALE_URL,
            files={"image": image_file},
            headers={"X-IMGGEN-KEY": API_KEY}
        )

    # ✅ Debug: Print API Response
    print("📡 API Response Code:", response.status_code)
    print("📡 API Response Body:", response.text)

    # ✅ Check API Response
    if response.status_code == 200:
        result = response.json()

        if result.get("success"):
            # ✅ Convert Base64 Image to File
            enhanced_image_base64 = result.get("image")  # Base64-encoded image
            enhanced_image_filename = f"enhanced_{file.filename}"
            enhanced_image_path = os.path.join(PROCESSED_FOLDER, enhanced_image_filename)

            with open(enhanced_image_path, "wb") as f:
                f.write(base64.b64decode(enhanced_image_base64))

            print(f"✅ Image saved at: {enhanced_image_path}")

            # ✅ Provide Download Link
            return jsonify({
                "download_url": f"/download_enhanced/{enhanced_image_filename}"
            }), 200
        else:
            return jsonify({"error": "Image processing failed!"}), 500
    else:
        return jsonify({"error": f"API Request Failed! {response.text}"}), 500

# ✅ Route for Downloading the Enhanced Image
def download_enhanced_image(filename):
    return send_from_directory(PROCESSED_FOLDER, filename, as_attachment=True)
