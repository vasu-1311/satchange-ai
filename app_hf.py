"""
HuggingFace Spaces Entry Point
Run: python app_hf.py
Deploy: Push this repo to HuggingFace Spaces (FREE, no credit card)
"""
import subprocess, sys, os

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    subprocess.run([
        sys.executable, "-m", "uvicorn",
        "backend.app:app",
        "--host", "0.0.0.0",
        "--port", "7860",  # HuggingFace default port
    ])
