class ChatAgent:

    def __init__(self, llm_service):
        self.llm = llm_service

    def chat(self, prompt):
        return self.llm.generate(prompt)
