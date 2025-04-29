from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    response = requests.post(
        "http://localhost:11434/api/generate", # Ollama API endpoint
        json={
            "model": "llama2",
            "prompt": f"Summarize this concisely:\n\n{text}",
            "stream": False
        }
    )
    # Add error handling for the request
    response.raise_for_status() # Raises an exception for bad status codes
    
    result = response.json()
    # Add basic check for response content
    summary_text = result.get("response", "Error: No response field in Ollama output.")
    return {"summary": summary_text}
