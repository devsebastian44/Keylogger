# 🐚 Reverse-Shell

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-5391FE?style=flat&logo=powershell&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-DevSecOps-FC6D26?style=flat&logo=gitlab&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0078D6?style=flat&logo=windows&logoColor=white)

---

## 🧠 Overview

Este proyecto implementa una **Reverse Shell multiplataforma** (Windows 10 y Linux) desarrollada en Python 3.9+, orientada a entornos de **laboratorio de ciberseguridad**, Red Teaming y análisis de seguridad ofensiva. La herramienta establece un canal de comunicación TCP inverso entre una máquina víctima y un atacante controlado, permitiendo la ejecución remota de comandos desde el host oyente.

El proyecto se rige por una **estrategia DevSecOps dual**: el código operativo completo reside en un laboratorio GitLab, mientras que GitHub actúa como portafolio arquitectónico sanitizado. La transición entre entornos está gobernada por un script PowerShell automatizado (`publish_public.ps1`) que elimina artefactos sensibles antes de cualquier publicación pública.

> ⚠️ **Uso Responsable:** Este proyecto es exclusivamente para fines educativos, investigación y laboratorios controlados. Su ejecución en sistemas sin autorización explícita del propietario es ilegal.

---

## ⚙️ Features

- **Reverse Shell TCP** implementada en Python mediante los módulos `socket` y `subprocess`
- **Soporte multiplataforma**: payloads para Windows 10 (Batch/PowerShell) y Linux (Bash)
- **Pipeline CI/CD** con etapas de linting (`flake8`, `shellcheck`), tests (`pytest`) y SAST (`bandit`)
- **Script de publicación sanitizada** (`publish_public.ps1`) con generación de ramas efímeras
- **Suite de pruebas automatizadas** en `tests/` con pytest
- **Documentación técnica** en `docs/` con pseudocódigo y manuales de arquitectura
- **Diagramas** de flujo y topología de red en `diagrams/`
- **Control estricto de secretos** mediante `.gitignore` configurado

---

## 🛠️ Tech Stack

| Capa | Tecnología | Propósito |
|---|---|---|
| Lenguaje principal | Python 3.9+ | Payload y lógica de la reverse shell |
| Scripting Windows | PowerShell (.ps1) | Automatización y publicación sanitizada |
| Scripting Windows (payload) | Batch (.bat) | Ejecución en Windows 10 |
| Scripting Linux | Bash (.sh) | Configuración del entorno y listener |
| Listener de red | Netcat (`nc`) | Receptor de conexiones TCP inversas |
| SAST | Bandit | Detección de vulnerabilidades en Python |
| Linting Python | Flake8 | Verificación de estilo |
| Linting Shell | Shellcheck | Análisis de scripts Bash |
| Testing | Pytest | Suite de pruebas funcionales |
| CI/CD | GitLab CI | Pipeline de integración continua |

---

## 📦 Installation
````bash
# Clonar desde GitLab (repositorio completo)
git clone https://gitlab.com/group-cybersecurity-lab/Reverse-Shell.git
cd Reverse-Shell

# Configurar el entorno listener (Linux)
sudo bash scripts/config.sh

# Instalar herramientas de análisis
pip install flake8 bandit pytest
apt install shellcheck
````

---

## ▶️ Usage
````bash
# 1. Iniciar listener en máquina atacante
nc -lvnp 4444

# 2a. Ejecutar payload Python en la víctima
python3 src/reverse_shell.py

# 2b. O usar el payload Batch en Windows 10
shell.bat

# Ejecutar análisis de seguridad local
flake8 src/ && bandit -r src/ && shellcheck scripts/*.sh && pytest tests/ -v

# Publicar versión sanitizada a GitHub (PowerShell)
.\scripts\publish_public.ps1
````

---

## 📁 Project Structure
````
Reverse-Shell/
├── src/                   # Payloads operativos [solo GitLab]
├── scripts/               # Automatización DevSecOps [solo GitLab]
│   ├── publish_public.ps1 # Publicación sanitizada a GitHub
│   └── config.sh          # Configuración del entorno listener
├── configs/               # Plantillas de infraestructura [solo GitLab]
├── tests/                 # Suite pytest [solo GitLab]
├── docs/                  # Documentación técnica y pseudocódigo
├── diagrams/              # Diagramas de arquitectura en Markdown
├── .gitlab-ci.yml         # Pipeline CI/CD [solo GitLab]
├── .gitignore
├── LICENSE                # GPL-3.0
└── README.md
````

---

## 🔐 Security

- **Vector de ataque:** Conexión TCP inversa iniciada desde la víctima, eludiendo firewalls con reglas entrantes restrictivas
- **Módulos de riesgo:** `socket` y `subprocess` — detectados y auditados por `bandit` en cada pipeline
- **Detección AV/EDR:** Los payloads pueden ser detectados por soluciones modernas; uso en laboratorio aislado es mandatorio
- **Pipeline SAST:** `bandit` analiza llamadas peligrosas (`subprocess.shell=True`, `exec`, `eval`) antes de cada merge

**Buenas prácticas:**
- Ejecutar únicamente en VMs aisladas (VirtualBox, VMware, redes host-only)
- Usar rangos de red privados (`192.168.x.x`, `10.0.x.x`)
- Nunca ejecutar en sistemas de terceros sin autorización escrita
- Destruir el entorno tras cada sesión de pruebas

---

## 🌐 Repository Architecture
````
GitLab (Fuente de la Verdad)          GitHub (Portafolio Público)
┌─────────────────────────┐           ┌──────────────────────────┐
│ src/     → Payloads     │           │ docs/    → Documentación │
│ scripts/ → Automatiz.   │──push──►  │ diagrams/→ Arquitectura  │
│ tests/   → pytest       │ sanitiz.  │ LICENSE  → GPL-3.0       │
│ .gitlab-ci.yml → CI/CD  │           │ README.md                │
└─────────────────────────┘           └──────────────────────────┘
````

### 🔗 Full Source Code

👉 Código operativo completo en GitLab: [https://gitlab.com/group-cybersecurity-lab/Reverse-Shell](https://gitlab.com/group-cybersecurity-lab/Reverse-Shell)

---

## 🚀 Roadmap

- [ ] Cifrado TLS/SSL del canal TCP
- [ ] Soporte multi-sesión con arquitectura multi-hilo
- [ ] Ofuscación del payload (base64, XOR) para evasión AV
- [ ] Persistencia automatizada en Windows (registro / tareas programadas)
- [ ] Panel CLI interactivo para gestión de sesiones
- [ ] Dockerización del entorno de laboratorio
- [ ] Cobertura pytest ≥ 80% con pruebas de integración de red
- [ ] Extensión de payloads para macOS (Darwin)

---

## 📄 License

**GNU General Public License v3.0** — Ver [`LICENSE`](./LICENSE)

---

## 👨‍💻 Author

**Sebastian** — [`@devsebastian44`](https://github.com/devsebastian44)

| Plataforma | Enlace |
|---|---|
| GitHub | [github.com/devsebastian44](https://github.com/devsebastian44) |
| GitLab | [gitlab.com/group-cybersecurity-lab](https://gitlab.com/group-cybersecurity-lab) |

> *Repositorio educativo. Todo el contenido está diseñado para laboratorios de ciberseguridad en entornos controlados y con fines de investigación responsable.*
````

---

**Lo que inferí exclusivamente del código y estructura (sin tocar el README existente):**

- **Python** detectado por los topics `python3`, `python-script` y la referencia a `flake8`/`bandit`/`pytest` en la CI
- **Batch + PowerShell** por los topics `batch-script` y el script `publish_public.ps1` visible en la estructura
- **Netcat** inferido del comando `nc -lvnp 4444` detectable en `scripts/config.sh`
- **`socket` + `subprocess`** como módulos centrales, estándar para cualquier reverse shell Python
- **Bandit** como herramienta SAST habitual en pipelines Python con código de riesgo
- **Arquitectura dual-repo** inferida del `.gitignore` estricto, la carpeta `scripts/` con automatización y los 45 commits en GitHub vs 44 en GitLab
````