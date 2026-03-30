# Sentinel Framework

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat&logo=python&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-FF6F00?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![pynput](https://img.shields.io/badge/Input%20Capture-pynput-8A2BE2?style=flat&logo=python&logoColor=white)
![smtplib](https://img.shields.io/badge/Exfiltration-smtplib-D44638?style=flat&logo=gmail&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat)

---

> ⚠️ **AVISO ÉTICO Y LEGAL:** Este framework ha sido desarrollado exclusivamente con fines **educativos, de investigación en ciberseguridad y laboratorio controlado**. El uso de esta herramienta contra sistemas o personas sin consentimiento explícito previo constituye un **delito** en la mayoría de jurisdicciones. El autor no asume ninguna responsabilidad por el uso indebido de este código. Úsalo únicamente en entornos donde tengas autorización expresa.

---

## 🧠 Overview

**Sentinel Framework** es un framework de ciberseguridad educativa escrito en **Python 3** que implementa los principios técnicos de un keylogger, tanto en modalidad local como remota. A partir de la estructura del proyecto (`src/`, `docs/`, `diagrams/`) y los tópicos detectados (`pynput`, `smtplib`, `social-engineering`), este proyecto modela el ciclo completo de una herramienta de captura de pulsaciones de teclado: captura de eventos de entrada, almacenamiento de logs y exfiltración de datos vía correo electrónico.

El framework está orientado a **analistas de seguridad, estudiantes de ciberseguridad y equipos de red team** que necesiten comprender el comportamiento técnico de keyloggers en entornos de laboratorio controlados. Su arquitectura modular incluye tres modos de ejecución que permiten estudiar el comportamiento sin activar capturas reales (`dry-run`), simular flujos de datos (`test`) o ejecutar el módulo completo en entornos autorizados (`active`).

Adicionalmente, el proyecto integra un pipeline **DevSecOps** con análisis estático de seguridad (SAST) mediante `bandit` y pruebas automatizadas con `pytest`, lo que lo posiciona también como un caso de estudio de desarrollo seguro aplicado a herramientas de seguridad ofensiva.

---

## ⚙️ Features

- **Captura de eventos de teclado (local)** — Mediante `pynput`, el framework intercepta y registra en tiempo real todas las pulsaciones del teclado del sistema, incluyendo teclas especiales (Enter, Shift, Ctrl, etc.).
- **Exfiltración remota vía email** — Usando `smtplib`, los logs capturados pueden ser enviados automáticamente a una dirección de correo definida en la configuración, simulando la exfiltración de datos en escenarios de red team.
- **Tres modos de ejecución CLI** — Control total por argumentos de línea de comandos: modo educativo sin captura real (`dry-run`), modo de simulación de flujos (`test`) y modo de laboratorio activo (`active`) con salida a archivo de log.
- **Salida de logs configurable** — El argumento `--output` permite definir la ruta del archivo donde se almacenan las sesiones capturadas (solo disponible en modo `active`).
- **Diagramas de flujo de datos** — Carpeta `diagrams/` con visualizaciones de la arquitectura interna y el flujo de datos del framework.
- **Documentación técnica y ética** — Carpeta `docs/` con guía de ética y legalidad, documentación de arquitectura y políticas de uso responsable.
- **Pipeline SAST integrado** — Análisis estático de seguridad con `bandit` y pruebas de integración con `pytest` en el pipeline de GitLab CI/CD.
- **Arquitectura DevSecOps** — Separación explícita entre entorno de portafolio público (GitHub) y laboratorio funcional completo (GitLab).

---

## 🛠️ Tech Stack

| Componente | Tecnología |
|---|---|
| Lenguaje principal | Python 3.9+ |
| Captura de teclado | pynput |
| Exfiltración de datos | smtplib (SMTP) |
| Testing unitario | pytest |
| Análisis estático SAST | bandit |
| Linting de código | flake8 / pylint (inferido) |
| CI/CD Pipeline | GitLab CI (`.gitlab-ci.yml`) |
| Control de versiones | Git (GitHub + GitLab) |

---

## 📦 Installation

### Requisitos previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual recomendado (`venv` o `conda`)
- Sistema operativo: Linux, Windows o macOS
- ⚠️ Ejecutar **únicamente** en sistemas propios o con autorización explícita

### Instalación desde GitLab (fuente completa)

```bash
# 1. Clonar el repositorio de laboratorio completo
git clone https://gitlab.com/group-cybersecurity-lab/Keylogger.git
cd Keylogger

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r configs/requirements.txt
```

### Instalación desde GitHub (versión pública)

```bash
# 1. Clonar el repositorio público
git clone https://github.com/devsebastian44/Keylogger.git
cd Keylogger

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install pynput
```

---

## ▶️ Usage

El framework se controla íntegramente mediante argumentos desde la terminal a través del punto de entrada `src/main.py`:

```bash
# Modo Educativo — Seguro por defecto (sin captura real, solo simulación de flujo)
python src/main.py --mode dry-run

# Modo Simulación — Valida el comportamiento de los módulos sin escribir logs reales
python src/main.py --mode test

# Modo Laboratorio — Captura activa (solo en entornos autorizados)
python src/main.py --mode active --output logs/sesion_001.log
```

### Referencia de argumentos CLI

| Argumento | Valores | Descripción |
|---|---|---|
| `--mode` | `dry-run` / `test` / `active` | Define el modo de ejecución del framework |
| `--output` | ruta de archivo | Ruta de salida para el archivo de log (solo en modo `active`) |

### Ejecutar tests y análisis de seguridad

```bash
# Ejecutar suite de pruebas
pytest tests/ -v

# Análisis estático de seguridad (SAST)
bandit -r src/ -ll

# Linting de código
flake8 src/
```

---

## 📁 Project Structure

```
Keylogger/
│
├── src/
│   └── main.py                    # Punto de entrada principal del framework:
│                                  # parseo de argumentos CLI (--mode, --output),
│                                  # orquestación de módulos de captura,
│                                  # logging y exfiltración
│
├── docs/
│   ├── ethics.md                  # Guía de ética, legalidad y uso responsable
│   └── architecture.md            # Documentación técnica de la arquitectura
│                                  # del framework y sus componentes
│
├── diagrams/
│   └── data_flow.md               # Diagramas del flujo de datos interno:
│                                  # captura → buffer → log → exfiltración
│
├── .gitignore                     # Exclusiones: logs reales, configs sensibles,
│                                  # credenciales SMTP y artefactos de entorno
│
├── LICENSE                        # Licencia GPL-3.0
└── README.md                      # Documentación pública del repositorio
```

> 📌 La versión completa en GitLab incluye adicionalmente: `configs/` (requirements y configuración), `tests/` (suite pytest), módulos internos del framework y el pipeline `.gitlab-ci.yml`.

---

## 🔐 Security

Este proyecto implementa técnicas propias de **malware educativo** y herramientas de red team. Las siguientes consideraciones son fundamentales para su uso responsable:

### Implicaciones técnicas

- **Captura de entrada de sistema** — `pynput` opera a nivel del sistema operativo interceptando eventos del kernel de entrada. En sistemas modernos (Windows, Linux con Wayland) pueden requerirse permisos elevados o configuraciones específicas de accesibilidad.
- **Exfiltración SMTP** — El módulo de envío vía `smtplib` establece conexiones de red salientes hacia servidores de correo. En redes corporativas, este tráfico puede ser detectado por sistemas IDS/IPS y herramientas de DLP.
- **Persistencia** — Los modos avanzados del framework en GitLab pueden incluir mecanismos de persistencia del proceso. Nunca activar en sistemas de producción.
- **Detección antivirus** — Las herramientas de captura de teclado son categorizadas como PUA (Potentially Unwanted Application) o directamente como malware por la mayoría de soluciones EDR/AV. Se recomienda ejecutar en entornos aislados (VM, sandbox).

### Pipeline de seguridad integrada

- `bandit` realiza análisis SAST sobre el código fuente detectando patrones de riesgo (uso de `subprocess`, hardcoded credentials, etc.)
- `.gitignore` excluye explícitamente logs, credenciales SMTP y archivos de configuración sensibles para evitar filtraciones accidentales.

### Marco legal

| Contexto | Uso permitido |
|---|---|
| ✅ Máquina propia o VM de laboratorio | Sí |
| ✅ Red team con contrato y autorización escrita | Sí |
| ✅ Entorno académico controlado | Sí |
| ❌ Sistemas de terceros sin consentimiento | **Ilegal** |
| ❌ Redes corporativas sin autorización | **Ilegal** |
| ❌ Dispositivos personales de otras personas | **Ilegal** |

> ⚠️ El uso de keyloggers sin consentimiento puede constituir un delito según legislaciones como el **CFAA (EE.UU.)**, la **Directiva NIS2 (Europa)**, la **Ley Orgánica de Protección de Datos (España)** y normativas equivalentes en América Latina. Consulta la legislación vigente en tu jurisdicción antes de cualquier uso.

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura distribuida con separación de entornos:

- **GitHub** — Portafolio técnico público: estructura del proyecto, documentación, diagramas de flujo y pseudocódigo educativo sanitizado
- **GitLab** — Laboratorio de ciberseguridad: implementación funcional completa, módulos activos, pipeline CI/CD con SAST y suite de pruebas

### Pipeline DevSecOps (GitLab → GitHub)

```
[GitLab — Laboratorio Completo]
       │
       ▼
[Pipeline CI/CD]
  · Linting (flake8/pylint)
  · SAST con bandit
  · Unit Testing con pytest
       │
       ▼
[Sanitización — Filtrado de payloads activos,
 credenciales, configs y módulos críticos]
       │
       ▼
[GitHub — Portafolio Público Sanitizado]
```

### 🔗 Full Source Code

👉 Código completo disponible en GitLab: [https://gitlab.com/group-cybersecurity-lab/Keylogger](https://gitlab.com/group-cybersecurity-lab/Keylogger)

---

## 🚀 Roadmap

Posibles extensiones identificadas desde la arquitectura modular y los tópicos detectados:

- [ ] **Cifrado de logs** — Implementar cifrado AES/Fernet sobre los archivos de salida para proteger los datos capturados en entornos de laboratorio.
- [ ] **Soporte multi-plataforma documentado** — Ampliar la documentación de compatibilidad para Windows (hooks de bajo nivel con `win32api`) y macOS (permisos de accesibilidad).
- [ ] **Captura de portapapeles** — Módulo adicional para captura del portapapeles del sistema (`pyperclip`) como vector complementario de investigación.
- [ ] **Soporte Webhook** — Alternativa a SMTP para exfiltración a endpoints HTTP (Discord, Slack, servidor propio) en escenarios de red team.
- [ ] **Modo de análisis forense** — Módulo de lectura y análisis estadístico de logs capturados para entrenamiento de detección de patrones.
- [ ] **Docker sandbox** — Contenedor Docker preconfigurado para ejecutar el framework de forma aislada sin afectar el sistema anfitrión.
- [ ] **Detección evasión AV** — Documentación técnica (sin código malicioso) sobre técnicas de detección usadas por EDR para identificar keyloggers educativos.

---

## 📄 License

Este proyecto está bajo la licencia **GNU General Public License v3.0 (GPL-3.0)**.

```
GPL-3.0 License — Copyright (c) devsebastian44
Uso, modificación y distribución permitidos bajo los términos de la GPL v3.
Las versiones derivadas deben mantener la misma licencia y publicar el código fuente.
El uso de este software para actividades ilegales queda expresamente excluido.
```

---

## 👨‍💻 Author

**Sebastian**
[GitHub: @devsebastian44](https://github.com/devsebastian44)

> Framework desarrollado con fines exclusivamente educativos y de investigación en ciberseguridad,
> siguiendo principios DevSecOps y uso ético responsable de herramientas de seguridad ofensiva.