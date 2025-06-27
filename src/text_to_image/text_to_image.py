import os
from flask import request, jsonify
from together import Together
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Get API key from environment variable
API_KEY = os.getenv('TOGETHER_API_KEY')

# ✅ Initialize Together client
client = None
if API_KEY:
    try:
        client = Together(api_key=API_KEY)
    except Exception as e:
        print(f"Error initializing Together client: {str(e)}")

# ✅ Text-to-Image Function for Flask
def process_text_to_image():
    if not API_KEY:
        return jsonify({'error': 'Together API key not configured!'}), 500

    try:
        prompt = request.form.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        response = client.images.generate(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell-Free",
            width=1280,  
            height=768,  
            steps=4, 
            n=1,
            response_format="b64_json"
        )

        # ✅ Extract Base64 image data
        image_data = response.data[0].b64_json

        # ✅ Return the image data to frontend
        return jsonify({'image': f"data:image/png;base64,{image_data}"})
    
    except Exception as e:
        return jsonify({'error': f"Error generating image: {str(e)}"}), 500
