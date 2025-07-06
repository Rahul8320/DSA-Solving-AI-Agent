from dotenv import load_dotenv
import os

class Settings:
    """Load environment variables and set them into respected variables"""
    load_dotenv()
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

    DEFAULT_PYTHON_IMAGE: str = "python:3-slim"
    DOCKER_WORK_DIR: str = "temp"
    CODE_EXECUTION_TIMEOUT: int = 120
    TERMINATION_KEYWORD: str = "STOP"
    TEAM_MAX_TURNS:int = 10