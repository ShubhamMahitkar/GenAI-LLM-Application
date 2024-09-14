from flask import Flask, request, jsonify
from transformers import pipeline
from flasgger import Swagger
import logging

app = Flask(__name__)
Swagger(app)

# Load pre-trained model
generator = pipeline('text-generation', model='gpt2')

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/generate', methods=['POST'])
def generate_text():
    """
    Generate text based on a prompt
    ---
    parameters:
      - name: body
        in: body
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "Once upon a time"
        required: true
        description: The input prompt for text generation
    responses:
      200:
        description: Generated text
      400:
        description: Invalid input
    """
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Generate text from the prompt
        result = generator(prompt, max_length=100, num_return_sequences=1)
        logging.info(f"Generated text for prompt: {prompt}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
