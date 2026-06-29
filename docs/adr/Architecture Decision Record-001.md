ADR-001 Arquitectura basada en Componentes

Estado: Aceptado

Problema
Si todo el código vive en main.py, el proyecto crecerá rápidamente y será imposible mantenerlo.

Decisión
El sistema estará dividido en componentes independientes.

Ejemplos:
•	Providers 
•	Services 
•	Agents 
•	Memory 
•	Skills 
•	Rules 

Cada componente tendrá una sola responsabilidad.

Consecuencias
Positivas
✔ Fácil mantenimiento.
✔ Fácil reemplazo.
✔ Fácil depuración.

Negativas
❌ Más archivos.
❌ Mayor diseño inicial.
