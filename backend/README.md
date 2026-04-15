# 🧠 Smart File Organizer - Backend

Python backend for Smart File Organizer Pro.

## 🤖 AI Setup (Ollama)

This project requires [Ollama](https://ollama.com/) for local LLM features.

1.  **Install Ollama**:
    - **Linux**: Run `bash scripts/install_ollama.sh` or follow instructions on the website.
    - **macOS/Windows**: Download the installer from [ollama.com](https://ollama.com/download).

2.  **Pull the Model**:
    ```bash
    ollama pull llama3.2
    ```

3.  **Verify Status**:
    Ensure the Ollama server is running (usually at `http://localhost:11434`).

## 🚀 Setup

1.  **Install Poetry**:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2.  **Install dependencies**:
    ```bash
    poetry install
    ```

3.  **Run with Uvicorn**:
    ```bash
    poetry run uvicorn api.server:app --reload
    ```
