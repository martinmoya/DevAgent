ADR-014 Comunicación mediante Objetos Tipados

Estado: Aceptado

Problema
El intercambio de información mediante diccionarios dificulta el mantenimiento y aumenta la probabilidad de errores.

Decisión
Los componentes intercambiarán únicamente objetos tipados (DTO).

Consecuencias positivas
•	Autocompletado en el IDE. 
•	Mayor claridad del código. 
•	Validación sencilla. 
•	Menor acoplamiento con estructuras internas. 

Consecuencias negativas
•	Es necesario definir clases adicionales. 
