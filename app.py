# Import Dependencies
import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="StudyPal",
    page_icon="📜",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"
)

# Set the title of the app
st.title("📜 StudyPal Application")

# API Details
API_ENDPOINT = "http://127.0.0.1:8000/ask"
providers = ["Groq", "Ollama"]
models = ["llama 3.3", "deepseek R1"]

# Initialize session state variables
# Default values of variables when the page is loaded for the first time
st.session_state.setdefault("question", "")
st.session_state.setdefault("show_settings", False)
st.session_state.setdefault("provider", providers[0])
st.session_state.setdefault("model", models[0])

# Layout
col1, col2 = st.columns([8, 1])

# Create a text input for the user to ask a question
question = col1.text_input(label="Ask a question:", placeholder="Type your question here...")

if col2.button("🦾", help="Select model settings"):
    # Toggle the settings expander
    st.session_state.show_settings = not st.session_state.show_settings
# Model Settings Expander
if st.session_state.show_settings:
    with st.expander("🔧 Model Settings", expanded=True):
        # Create a select box for the user to select a provider
        st.session_state.provider = st.selectbox(label="Select a provider:", options=providers, index=providers.index(st.session_state.provider))

        # Create a select box for the user to select a model
        st.session_state.model = st.selectbox(label="Select a model:", options=models, index=models.index(st.session_state.model))

        # Success message
        st.success(f"Provider: {st.session_state.provider}, Model: {st.session_state.model}")

# Create a button to submit the question and get an answer from the API
if st.button("Submit", help="Submit your question to the model"):
    # Check if the question is not empty
    if question:
        # Update the session state with the question
        st.session_state.question = question

        # Display a loading message while waiting for the API response
        with st.spinner("Waiting for response..."):
            # Call the API and get the answer
            # Create a payload for the request
            payload = {
                "question": question
            }
            # Send a POST request to the API endpoint with the payload
            response = requests.post(API_ENDPOINT, json=payload)
            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                # Get the answer from the response JSON
                answer = response.json().get("answer")
                # Display the answer in the app
                st.success(answer)
            else:
                # Display an error message if the request failed
                st.error("Error: Unable to get a response from the API.")

    else:
        # Display an error message if the question is empty
        st.error("Please enter a question.")


# Run
# streamlit run C:\nima\studypalf\app.py