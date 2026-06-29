ADR-017 Uso de una Factory para la creación de proveedores LLM.

Estado: Aceptado.

Problema
El resto del sistema no debe conocer qué proveedor concreto de IA se está utilizando.

Decisión
Toda creación de proveedores se centralizará en LLMFactory.

Consecuencias positivas
Un único punto de creación.
Fácil cambio entre LM Studio y Ollama.
El resto del sistema permanece desacoplado.

Consecuencias negativas
La implementación inicial usa if/elif, lo que requerirá una mejora futura cuando existan muchos proveedore