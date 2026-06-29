ADR-003 Factory Pattern

Estado: Aceptado

Problema
No queremos escribir esto:
if provider == ...
en veinte archivos distintos.

Decisión
Existirá un Factory para construir objetos.

Consecuencia
Cambiar LM Studio por Ollama requerirá modificar solamente .env.
