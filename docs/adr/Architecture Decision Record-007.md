ADR-007 Service Layer

Estado: Aceptado

Problema
Los agentes no deben conocer implementaciones concretas.

Decisión
Los agentes únicamente interactuarán con servicios.

Consecuencia
Será posible reemplazar MySQL por PostgreSQL sin modificar agentes.
