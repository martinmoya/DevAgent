# DevAgent

> Framework de Ingeniería de Software Asistido por Inteligencia Artificial.

---

## Descripción

DevAgent es un framework desarrollado en Python cuyo objetivo es asistir en el ciclo completo de desarrollo de software mediante el uso de modelos de lenguaje (LLM).

Actualmente soporta proveedores compatibles con la API de OpenAI (como LM Studio y Ollama), con una arquitectura desacoplada que permitirá incorporar nuevos proveedores en el futuro.

Este proyecto tiene como objetivo evolucionar desde un simple cliente para LLM hasta convertirse en una plataforma completa para ingeniería de software asistida por IA.

---

## Estado del proyecto

Versión actual:

**v0.1.0**

Estado:
✅ MVP Funcional

Actualmente es capaz de:

- Conectarse a LM Studio
- Conectarse a Ollama
- Detectar el proveedor configurado
- Enviar prompts al modelo
- Mostrar las respuestas
- Cambiar de proveedor mediante configuración

---

## Arquitectura actual

```
                main.py
                    │
                    ▼
                Kernel
                    │
                    ▼
              LLMFactory
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 LMStudioProvider       OllamaProvider
        │                       │
        ▼                       ▼
     LM Studio              Ollama
```

---

## Estructura del proyecto

```
DevAgent/

├── agents/
├── config/
│   └── settings.py
│
├── core/
│   ├── banner.py
│   ├── kernel.py
│   ├── logger.py
│   ├── exceptions.py
│   └── application.py
│
├── factories/
│   └── llm_factory.py
│
├── providers/
│   ├── base.py
│   ├── lmstudio.py
│   └── ollama.py
│
├── services/
├── tests/
├── docs/
├── logs/
│
├── main.py
├── requirements.txt
├── devagent.env
└── README.md
```

---

## Requisitos

- Python 3.14+
- LM Studio o Ollama
- pip

---

## Instalación

Crear entorno virtual

Windows

```bash
python -m venv .venv
```

Activar entorno

```bash
.venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Archivo de configuración

Crear un archivo llamado:

```
devagent.env
```

Ejemplo:

```ini
LLM_PROVIDER=lmstudio
LLM_HOST=http://127.0.0.1:1234/v1
MODEL=meta-llama-3-8b-instruct
TEMPERATURE=0.2
MAX_TOKENS=4096
```

---

## Ejecución

```bash
python main.py
```

Salida esperada

```
============================================================
DevAgent v0.1.0
============================================================

Proveedor conectado correctamente.

Escribe 'exit' para salir.

> Hola

¡Hola! ¿En qué puedo ayudarte hoy?
```

---

## Roadmap

### v0.1

- [x] Kernel
- [x] Providers
- [x] Factory
- [x] Configuración
- [x] Integración con LM Studio

### v0.2

- [ ] Logger profesional
- [ ] Manejo de excepciones
- [ ] Validación de configuración

### v0.3

- [ ] ChatAgent
- [ ] Historial de conversación

### v0.4

- [ ] PromptEngine

### v0.5

- [ ] Skills

### v0.6

- [ ] Rules

### v0.7

- [ ] Memory

### v0.8

- [ ] MySQL

### v0.9

- [ ] MCP (Model Context Protocol)

### v1.0

- [ ] Framework estable

---

## Objetivos del proyecto

- Arquitectura desacoplada
- Código limpio (Clean Code)
- Principios SOLID
- Clean Architecture
- Fácil extensión
- Fácil mantenimiento
- Compatible con múltiples LLM

---

## Licencia

Pendiente de definir.

---

## Autor

Proyecto desarrollado como parte de un proceso de aprendizaje y construcción de un framework de ingeniería de software asistido por IA.

Autor:

Martin Moya Hernandez

Asistencia técnica y diseño de arquitectura:

OpenAI ChatGPT