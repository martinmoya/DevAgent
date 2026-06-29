from config.settings import Settings

from providers.lmstudio import LMStudioProvider
from providers.ollama import OllamaProvider


class LLMFactory:

    @staticmethod
    def create():

        provider = Settings.PROVIDER.lower()

        if provider == "lmstudio":
            return LMStudioProvider()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Proveedor no soportado: {provider}"
        )