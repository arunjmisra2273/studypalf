# Import Dependencies
import streamlit as st
import requests

# Set the page configuration
st.set_page_config(
    page_title="StudyPal",
    page_icon="📜", # We should use emojidb.org for emojis
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"    # or "collapsed"
)

# Set the title of the app
st.title("📜 StudyPal Application")

# set the api endpoint
api_endpoint = "http://127.0.0.1:8000/ask"

# Create a text input for the user to ask a question
question = st.text_input(label="Ask a question:", placeholder="Type your question here...")

# Create a button to submit the question
if st.button("Get Answer"):
    # Display a message indicating that the question is being processed
    st.info("Processing your question...")
    # Check if the question is not empty
    if question:
        # Create a payload for the request
        payload = {
            "question": question
        }
        # Send a POST request to the API endpoint with the payload
        response = requests.post(api_endpoint, json=payload)
        
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
        # Display a warning message if the question is empty
        st.warning("Please enter a question before submitting.")

# Run
# streamlit run C:\nima\studypalf\app.py