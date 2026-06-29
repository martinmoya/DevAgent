from abc import ABC, abstractmethod

class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def list_models(self):
        pass

    @abstractmethod
    def health(self):
        pass
