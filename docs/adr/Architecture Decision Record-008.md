ADR-008 Encapsulamiento de proveedores

Estado: Aceptado

Problema
El resto del sistema no debe conocer cómo funciona la API específica de cada proveedor de IA.

Decisión
Cada proveedor encapsulará toda la lógica de comunicación (conexión, comprobación de estado, listado de modelos y generación de respuestas) detrás de una interfaz común (BaseLLMProvider).

Consecuencias positivas
•	Cambiar de LM Studio a Ollama no afecta al resto del código. 
•	Es posible crear proveedores para OpenAI, Gemini u otros sin modificar los agentes. 
•	Las pruebas unitarias son más sencillas porque se pueden simular proveedores. 

Consecuencias negativas
•	Hay que escribir una pequeña cantidad de código adicional por cada nuevo proveedor. 
