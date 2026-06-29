import ollama

from config.settings import Settings
from providers.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

    def __init__(self):

        self.client = ollama.Client(
            host=Settings.OLLAMA_URL
        )

    def connect(self):

        pass

    def health(self):

        try:
            self.client.list()
            return True
        except Exception:
            return False

    def list_models(self):

        models = self.client.list()

        return [
            model["model"]
            for model in models["models"]
        ]

    def generate(self, prompt: str) -> str:

        response = self.client.chat(
            model=Settings.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
    