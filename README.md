# LLaMA Text Summarizer

Text Summarizer AI project using LLaMA via Ollama. Integrated with FastAPI for the backend and Streamlit for the frontend.

## Overview

*   **Goal**: Build a Text Summarization App using a locally hosted LLaMA model via Ollama.
*   **Tech Stack**:
    *   Ollama – Run LLaMA locally
    *   FastAPI – Backend API to interact with the model
    *   Streamlit – Frontend UI
    *   Git/GitHub – Version control & repo hosting

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/ashish-kj/TextSummarizer.git
    cd text-summarizer-llama
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install and run Ollama:**
    *   Download and install Ollama: [https://ollama.com](https://ollama.com)
    *   Pull the LLaMA model (ensure Ollama is running):
        ```bash
        ollama pull llama2
        ```

## Running the Application

1.  **Run the FastAPI backend:**
    *   Navigate to the project root directory in your terminal (where `backend` folder is located).
    *   Make sure your virtual environment is activated.
    *   Run the server:
        ```bash
        uvicorn backend.main:app --reload
        ```
    *   The API will be available at `http://localhost:8000`.

2.  **Run the Streamlit frontend:**
    *   Open a *new* terminal window/tab.
    *   Navigate to the project root directory.
    *   Make sure your virtual environment is activated.
    *   Run the app:
        ```bash
        streamlit run frontend/app.py
        ```
    *   The frontend will open in your browser, likely at `http://localhost:8501`.

## Project Structure

```
text-summarizer-llama/
│
├── backend/
│   └── main.py       # FastAPI application
│
├── frontend/
│   └── app.py        # Streamlit application
│
├── venv/             # Virtual environment directory (ignored by Git)
│
├── requirements.txt  # Python dependencies
└── README.md         # This file
```
