ADR-004 Dependency Injection

Estado: Aceptado

Problema
Los componentes no deben depender de implementaciones concretas.

Decisión
Todas las dependencias serán inyectadas mediante interfaces.

Consecuencia
Será posible cambiar cualquier implementación sin modificar el código consumidor.
