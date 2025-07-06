from autogen_ext.models.ollama import OllamaChatCompletionClient

from configs.settings import Settings


def get_ollama_client() -> OllamaChatCompletionClient:
    """
        Get an instance of ollama client

        Return:
            An instance of ollama chat completion client
    """
    ollama_client = OllamaChatCompletionClient(model=Settings.OLLAMA_MODEL, host=Settings.OLLAMA_URL)
    return ollama_client