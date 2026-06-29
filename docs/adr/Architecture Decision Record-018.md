ADR-018 Kernel como Orquestador

Estado: Aceptado

Problema
Debe existir un único punto responsable del ciclo de vida de la aplicación.

Decisión
Se crea Kernel, encargado de inicializar, ejecutar y finalizar DevAgent.

Responsabilidades
•	Inicializar componentes. 
•	Validar que el proveedor esté disponible. 
•	Ejecutar el ciclo principal. 
•	Finalizar correctamente la aplicación. 

No debe hacer
•	Construir prompts. 
•	Acceder directamente a MySQL. 
•	Analizar código. 
•	Implementar lógica de negocio. 
•	Comunicarse directamente con APIs externas (eso corresponde a los Providers). 

Consecuencias positivas
•	Punto único de control. 
•	Fácil depuración. 
•	Fácil ampliación. 

Consecuencias negativas
•	Si en el futuro acumula demasiadas responsabilidades, habrá que dividir parte de la lógica en servicios especializados. 
