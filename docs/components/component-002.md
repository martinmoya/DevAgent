COMPONENTE 002

Nombre: LMStudioClient

Responsabilidad
Hablar exclusivamente con la API compatible OpenAI que expone LM Studio.

No debe hacer
❌ Saber qué agente hizo la consulta.
❌ Construir prompts.
❌ Guardar conversaciones.
❌ Conocer Skills.
❌ Conocer MCP.

Entrada
prompt
modelo
temperatura

Salida
texto
Nada más.

Dependencias
OpenAI SDK
Logger
Config
