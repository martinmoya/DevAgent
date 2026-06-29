from agents.chat_agent import ChatAgent
from services.llm_service import LLMService

class AgentFactory:

    @staticmethod
    def create_chat():
        llm = LLMService()
        return ChatAgent(llm)
