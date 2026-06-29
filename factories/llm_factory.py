from config.settings import Settings

class LLMFactory:

    @staticmethod
    def create():
        provider = Settings.PROVIDER.lower()

        if provider == "lmstudio":
            from providers.lmstudio import LMStudioProvider
            return LMStudioProvider()

        elif provider == "ollama":
            from providers.ollama import OllamaProvider
            return OllamaProvider()

        raise ValueError(f"Proveedor no soportado: {provider}")

