ADR-005 Kernel

Estado: Aceptado

Problema
No existe un punto central para inicializar la aplicación.

Decisión
Todo componente será inicializado por el Kernel.

Consecuencias
Positivas
•	Punto único de arranque. 
•	Fácil depuración. 
•	Fácil apagado. 

Negativas
•	Kernel más complejo. 
