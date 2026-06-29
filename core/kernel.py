from core.banner import show
from factories.llm_factory import LLMFactory

class Kernel:

    def __init__(self):
        self.provider = None

    def initialize(self):
        show()
        self.provider = LLMFactory.create()
        self.provider.connect()

        if not self.provider.health():
            raise Exception("No fue posible conectar con el proveedor.")

        print("Proveedor conectado correctamente.\n")

    def run(self):
        print("Escribe 'exit' para salir.\n")

        while True:
            prompt = input("> ")

            if prompt.lower() == "exit":
                break

            try:
                response = self.provider.generate(prompt)
                print()
                print(response)
                print()

            except Exception as ex:
                print(f"\nERROR: {ex}\n")

    def shutdown(self):
        print("\nApagando DevAgent...")
