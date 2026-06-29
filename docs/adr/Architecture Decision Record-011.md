ADR-011 Constructor Injection

Estado: Aceptado

Problema
Los componentes crean internamente sus dependencias.

Decisión
Las dependencias serán recibidas mediante el constructor.

Consecuencia
Mayor facilidad para realizar pruebas unitarias.
