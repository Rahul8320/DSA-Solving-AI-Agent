from dotenv import load_dotenv
import os

class Settings:
    """Load environment variables and set them into respected variables"""
    load_dotenv()
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = "llama3.2:1b"