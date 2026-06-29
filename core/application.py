from dataclasses import dataclass

@dataclass
class Application:
    name: str = "DevAgent"
    version: str = "0.1.0"
    author: str = "Martin Moya"
    architecture: str = "Multi-Agent"
    llm: str = "LM Studio"
