ADR-002 Providers

Estado: Aceptado

Problema
El sistema deberá soportar varios LLM.

Hoy:
LM Studio

Mañana:
Ollama

Después:
OpenAI

Después:
Gemini

Decisión
Todo proveedor implementará exactamente la misma interfaz.
generate()
health()
list_models()

Consecuencias
El resto del proyecto nunca sabrá qué proveedor utiliza.
