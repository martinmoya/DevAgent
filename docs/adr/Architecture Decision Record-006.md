ADR-006 Registry Pattern

Estado: Aceptado

Problema
Kernel no debe conocer todos los componentes existentes.

Decisión
Se crea un Registry encargado de registrar dinámicamente:
•	Providers 
•	Services 
•	Agents 
•	Plugins 

Consecuencia
Agregar un nuevo componente no requiere modificar Kernel.
