# GEMINI Image Demo

This repository demonstrates an application using the GEMINI API for generating descriptive responses about images based on user input prompts.

## Overview

The application is built using Streamlit, a Python framework for creating web applications. It integrates with the GEMINI API from Google Generative AI to provide textual descriptions of images uploaded by users.

## Features

- **Input Prompt**: Users can provide a text prompt to guide the AI in generating descriptions.
- **Image Upload**: Supports uploading JPG, JPEG, and PNG images for analysis.
- **Response Generation**: Upon clicking the "Tell me about the Image" button, the application sends the image and prompt (if provided) to the GEMINI model and displays the generated response.
- **Error Handling**: Errors during response generation are displayed to the user.

## Requirements

To run the application locally, ensure you have the following installed:

- Python 3.6+
- Required Python packages (`requirements.txt` will list them)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gemini-image-demo.git
   cd gemini-image-demo
2. Install dependencies:
pip install -r requirements.txt

3. Set up environment variables:
   Obtain an API key from GEMINI API (Google Generative AI).
   Set this key as an environment variable named GOOGLE_API_KEY.

4. Run the application:
streamlit run app.py
5. Access the application:
Open your web browser and go to http://localhost:8501 (or another URL provided by Streamlit).

## Usage
Upon running the application, you'll see an input field to enter a prompt and a file uploader to upload an image.
Upload an image and optionally enter a prompt.
Click on "Tell me about the Image" to generate a description.
The generated response will be displayed below the image.
## Example
![Screenshot 2024-06-26 004206](https://github.com/Subhradyuti/GEMINI-Image-Demo/assets/133640355/c4ce81a1-3c77-463d-af86-027b8d1b5470)
![image](https://github.com/Subhradyuti/GEMINI-Image-Demo/assets/133640355/cce3aa47-8529-42ce-97e1-2122a012fed2)

