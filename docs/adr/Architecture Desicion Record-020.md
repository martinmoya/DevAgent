ADR-020 El Agente es responsable del contexto

Estado: Aceptado.

Problema
Debe existir un único responsable de decidir qué información se envía al LLM.

Decisión
Los Agentes construirán el PromptContext. El PromptEngine únicamente ensamblará el prompt final.

Consecuencias
•	Los Agentes encapsulan la estrategia. 
•	El PromptEngine permanece genérico. 
•	Es posible reutilizar el mismo PromptEngine con cualquier tipo de agente. 
