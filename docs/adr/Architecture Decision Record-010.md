ADR-010 Logger como Servicio

Estado: Aceptado

Problema
El Logger será utilizado por todos los módulos.

Decisión
Se convierte en un Service.

Consecuencia
Podrá cambiarse fácilmente por:
Elastic
Grafana
OpenTelemetry

Sin modificar el resto del proyecto.
