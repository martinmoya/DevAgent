from openai import OpenAI

from config.settings import Settings
from providers.base import BaseLLMProvider


class LMStudioProvider(BaseLLMProvider):

    def __init__(self):

        self.client = None

    def connect(self):

        self.client = OpenAI(
            base_url=Settings.LMSTUDIO_URL,
            api_key="lm-studio"
        )

    def health(self):

        try:
            self.client.models.list()
            return True
        except Exception:
            return False

    def list_models(self):

        models = self.client.models.list()
        return [model.id for model in models.data]

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=Settings.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    