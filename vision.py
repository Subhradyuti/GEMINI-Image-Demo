import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure GEMINI API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro-vision')

# Function to get responses from GEMINI model
def get_gemini_response(input_text, image):
    try:
        if input_text:
            response = model.generate_content([input_text, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")

# Streamlit app setup
st.set_page_config(page_title="GEMINI Image Demo")
st.title("Gemini Applications")

# Input prompt for user
input_text = st.text_input("Input Prompt:")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Button to generate response
submit = st.button("Tell me about the Image")

# Display response when button is clicked
if submit:
    if image is not None:
        with st.spinner('Generating response...'):
            response = get_gemini_response(input_text, image)
            st.subheader("Response:")
            st.write(response)
    else:
        st.warning("Please upload an image.")
