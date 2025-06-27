import os
import cv2
import numpy as np
import pytesseract
import shutil
import re
from spellchecker import SpellChecker

# ✅ Dynamically find Tesseract OCR path
tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    raise FileNotFoundError("❌ Tesseract-OCR is not installed or not in your PATH. Please install it first.")

# ✅ Initialize SpellChecker
spell = SpellChecker()

# ✅ Preprocessing Function
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image at {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Deskew the image
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = gray.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(rotated, (5, 5), 0)

    # Use Otsu's thresholding
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary

# ✅ Text Extraction Function
def extract_text(image_path):
    print(f"➡️ Extracting text from: {image_path}")

    try:
        processed_img = preprocess_image(image_path)
    except Exception as e:
        raise ValueError(f"Image preprocessing failed: {e}")

    # Use --psm 3 for fully automatic page segmentation
    config = '--psm 3 -c preserve_interword_spaces=1'
    try:
        extracted_text = pytesseract.image_to_string(processed_img, config=config, lang='eng')
    except Exception as e:
        raise ValueError(f"Text extraction failed: {e}")

    if not extracted_text.strip():
        raise ValueError("No text detected. Please upload a clearer image with visible text.")

    print(f"✅ Extracted text:\n{extracted_text}")
    return extracted_text.strip()

# ✅ Text Correction Function
def correct_text(text):
    print("➡️ Correcting extracted text...")
    corrected_words = []

    for word in text.split():
        # Skip correction for non-alphabetic words or short symbols
        if len(word) > 1 and word.isalpha():
            corrected_word = spell.correction(word) or word
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)

    # Fix common spacing and punctuation issues
    corrected_text = ' '.join(corrected_words)
    corrected_text = re.sub(r'\s+([.,!?])', r'\1', corrected_text)
    corrected_text = re.sub(r'([a-zA-Z])\s+([.,!?])', r'\1\2', corrected_text)

    print(f"✅ Corrected text:\n{corrected_text}")
    return corrected_text

# ✅ Text Reconstruction Process
def process_text_reconstruction(input_path, output_path):
    try:
        print(f"➡️ Processing file: {input_path}")

        # Step 1: Extract text
        extracted_text = extract_text(input_path)

        # Step 2: Correct text
        corrected_text = correct_text(extracted_text)

        # Step 3: Save corrected text to file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(corrected_text)

        print(f"✅ Reconstructed text saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")
        raise e

# ✅ Example Usage
if __name__ == "__main__":
    input_file = 'input.jpg'
    output_file = 'corrected_output.txt'

    process_text_reconstruction(input_file, output_file)
    print(f"✅ Corrected text saved to: {output_file}")
