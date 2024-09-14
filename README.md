# GenAI Text Generation App

## Overview
This application demonstrates a basic text generation system using a pre-trained GenAI Large Language Model (GPT-2). It takes a user-provided prompt and generates text based on that input. The application is built using Flask for the backend and leverages the Hugging Face Transformers library for the language model.

## Features
- Accepts user input (prompt) via a POST request.
- Generates and returns text based on the input prompt using GPT-2.
- Includes Swagger API documentation.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- Git (optional, for cloning the repository)

### Installation
1. **Clone the repository** (or download it as a ZIP file):
    ```bash
    git clone https://github.com/ShubhamMahitkar/GenAI-LLM-Application.git
    cd genai-text-generation-app
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
1. **Start the Flask server**:
    ```bash
    python app.py
    ```

2. The server will run on `http://127.0.0.1:5000`. 

3. **Generate text**:
    - Send a POST request to the `/generate` endpoint with a JSON payload:
    
    Example using `curl`:
    ```bash
    curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'
    ```

    Expected response:
    ```json
    [
      {
        "generated_text": "Once upon a time in a land far away..."
      }
    ]
    ```

### Running with Docker
1. **Build the Docker image**:
    ```bash
    docker build -t genai-app .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5000:5000 genai-app
    ```

### API Documentation
- The API documentation is available via Swagger UI at `http://127.0.0.1:5000/apidocs`.

### Testing
- Run unit tests using:
    ```bash
    python test_app.py
    ```

## How It Works
1. The application uses the Hugging Face `pipeline` to load a pre-trained GPT-2 model.
2. When a POST request is sent to the `/generate` endpoint with a prompt, the model generates text based on that prompt.
3. The generated text is returned in JSON format.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Repository
- [GitHub Repository](https://github.com/ShubhamMahitkar/GenAI-LLM-Application.git)
