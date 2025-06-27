import os
from flask import Flask, render_template, request, send_file, send_from_directory  # ✅ Import send_from_directory
from dotenv import load_dotenv
from src.text_reconstructor.text_reconstructor import process_text_reconstruction
from src.image_enhancer.image_enhancer import process_image_enhancement
from src.text_to_image.text_to_image import process_text_to_image

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Flask App
app = Flask(__name__, template_folder="templates", static_folder="static")

# ✅ Route for Home Page
@app.route("/")
def index():
    return render_template("index.html")

# ✅ Route for Text Reconstruction
@app.route("/text_reconstruction", methods=["GET", "POST"])
def text_reconstruction():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename != "":
            file_path = os.path.join("src", "text_reconstructor", "uploads", file.filename)
            file.save(file_path)

            corrected_file_path = os.path.join("src", "text_reconstructor", "uploads", f"corrected_{file.filename}.txt")

            try:
                process_text_reconstruction(file_path, corrected_file_path)
                return {"download_url": f"/download_corrected_text/corrected_{file.filename}.txt"}
            except Exception as e:
                return {"error": f"Processing failed: {str(e)}"}

    return render_template("text_reconstruction/index.html")

# ✅ Route to Download Corrected Text File
@app.route("/download_corrected_text/<filename>", methods=["GET"])
def download_corrected_text(filename):
    corrected_file_path = os.path.join("src", "text_reconstructor", "uploads", filename)
    
    if os.path.exists(corrected_file_path):
        return send_file(corrected_file_path, as_attachment=True)

    return "No corrected file available", 404

# ✅ Route for Image Enhancement
@app.route("/image_enhancer", methods=["GET", "POST"])
def image_enhancer():
    if request.method == "POST":
        return process_image_enhancement()
    return render_template("image_enhancer/index.html")

# ✅ Route for Downloading Enhanced Image
@app.route('/download_enhanced/<filename>', methods=['GET'])
def download_enhanced(filename):
    processed_folder = os.path.abspath("src/image_enhancer/processed")  # ✅ Ensure correct absolute path

    # ✅ Check if file exists before sending
    file_path = os.path.join(processed_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(processed_folder, filename, as_attachment=True)

    return "❌ No enhanced image available", 404

# ✅ Route for Text to Image
@app.route("/text_to_image", methods=["GET", "POST"])
def text_to_image():
    if request.method == "POST":
        return process_text_to_image()
    return render_template("text_to_image/index.html")

# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
