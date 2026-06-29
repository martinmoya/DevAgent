ADR-021 Introducción de LLMService

Estado: Aceptado.

Problema
Los Agentes no deben depender directamente de los Providers.

Decisión
Crear un LLMService que encapsule el acceso a los modelos de lenguaje.

Consecuencias positivas
•	Los Agentes permanecen desacoplados de la infraestructura. 
•	Es posible añadir caché, métricas, reintentos o balanceo sin modificar los Agentes. 
•	La lógica de acceso al LLM queda centralizada. 

Consecuencias negativas
•	Se añade una capa adicional, aunque con una responsabilidad bien definida. 
