from dotenv import load_dotenv
import os

load_dotenv("devagent.env")

class Settings:
    PROVIDER = os.getenv("LLM_PROVIDER")
    LMSTUDIO_URL = os.getenv("LLM_HOST")
    MODEL = os.getenv("MODEL")
    TEMPERATURE = float(os.getenv("TEMPERATURE"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
