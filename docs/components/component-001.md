COMPONENTE 001

Nombre: LMStudioProvider

Responsabilidad
Hablar exclusivamente con LM Studio.

No debe hacer
❌ Leer MySQL
❌ Leer archivos
❌ Ejecutar Git
❌ Crear prompts
❌ Guardar memoria
❌ Saber qué agente hizo la consulta

Entrada
prompt: str

Salida
response: str

Dependencias
OpenAI SDK
Settings
Logger

Nada más.

Casos de uso
ArchitectAgent
ProgrammerAgent
TesterAgent
ReviewerAgent

Todos utilizarán este componente.
