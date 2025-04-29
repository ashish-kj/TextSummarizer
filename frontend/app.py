import streamlit as st
import requests

st.title("LLaMA Text Summarizer")

user_input = st.text_area("Enter text to summarize:", height=200)

if st.button("Summarize"):
    if user_input:
        try:
            # Assuming FastAPI backend runs on localhost:8000
            backend_url = "http://localhost:8000/summarize/"
            response = requests.post(backend_url, data={"text": user_input})
            
            # Check if the request was successful
            response.raise_for_status() 
            
            summary = response.json().get("summary", "Error: Could not parse summary from backend.")
            st.subheader("Summary:")
            st.write(summary)
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")
