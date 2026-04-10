# ⌨️ Keylogger — Framework de Captura de Keystrokes en Python

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/Exfiltración-SMTP%20%2F%20smtplib-orange?style=flat&logo=gmail&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-DevSecOps-FC6D26?style=flat&logo=gitlab&logoColor=white)
![SAST](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![Platform](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux-0078D6?style=flat&logo=windows&logoColor=white)

> ⚠️ **AVISO LEGAL Y ÉTICO:** Este proyecto es de uso **estrictamente educativo y para
> investigación en ciberseguridad defensiva**. Su ejecución en sistemas, dispositivos o
> redes sin la autorización explícita del propietario es **ilegal y constituye un delito**.
> El autor no se responsabiliza por ningún uso indebido de este software fuera de
> entornos controlados y autorizados. — _Extracto del LICENSE (GPL-3.0)_

---

## 🧠 Overview

Este proyecto es un **framework de captura de pulsaciones de teclado (keylogger)**
desarrollado íntegramente en Python 3.9+, orientado a laboratorios de investigación
en ciberseguridad, análisis de ingeniería social y comprensión de vectores de
exfiltración de datos en entornos controlados.

El framework está estructurado con un **sistema de modos de operación** controlados
por argumentos CLI (`--mode`), lo que permite ejecutarlo en modo de simulación segura
(`dry-run`) o en modo de pruebas (`test`) sin necesidad de acceder al entorno
operacional completo disponible exclusivamente en GitLab. El módulo `smtplib` de
Python, detectado entre los topics del repositorio, indica que el canal de exfiltración
de los logs capturados opera a través de **correo electrónico SMTP**, una técnica
documentada en la literatura de malware research que simula vectores de exfiltración
reales utilizados por amenazas persistentes avanzadas (APT).

El proyecto sigue la misma **arquitectura DevSecOps de doble repositorio** presente en
el resto del laboratorio del autor: el código fuente operacional completo reside en
GitLab (entorno privado), mientras que GitHub actúa como portafolio sanitizado con
la arquitectura, documentación y diagramas técnicos.

---

## ⚙️ Features

- **Sistema de modos de ejecución CLI** con tres niveles: `dry-run` (educativo/seguro,
  por defecto), `test` (simulación) y `active` (requiere acceso privado en GitLab).
- **Captura de pulsaciones de teclado** mediante escucha de eventos del sistema
  operativo, documentando keystrokes en tiempo real durante la sesión de laboratorio.
- **Canal de exfiltración vía SMTP** (`smtplib`) para el envío automatizado de logs
  capturados a una dirección de correo de laboratorio configurable.
- **Salida local de sesión** en archivos de log con nomenclatura estructurada
  (`logs/sesion_NNN.log`), configurable mediante el argumento `--output`.
- **Arquitectura modular** con separación entre lógica de captura (`src/`),
  documentación técnica (`docs/`) y diagramas de flujo (`diagrams/`).
- **Pipeline CI/CD en GitLab** con etapas de linting (`flake8`) y análisis estático
  de seguridad (`bandit`) como pasos obligatorios en cada ciclo de desarrollo.
- **Estrategia DevSecOps dual** con sanitización automatizada del repositorio
  público en GitHub antes de cada publicación.
- **Gestión estricta de secretos** mediante `.gitignore` que excluye credenciales
  SMTP, archivos de log y configuraciones de red.

---

## 🛠️ Tech Stack

| Categoría | Tecnología | Propósito |
|---|---|---|
| Lenguaje principal | Python 3.9+ | Lógica del framework completo |
| Captura de eventos | `keyboard` / eventos OS | Intercepción de pulsaciones de teclado |
| Exfiltración de datos | `smtplib` (stdlib) | Envío de logs vía correo SMTP |
| Interfaz CLI | `argparse` (stdlib) | Control de modos de ejecución |
| Almacenamiento local | Sistema de archivos | Logs de sesión en `logs/` |
| Linting | `flake8` | Validación de estilo de código |
| SAST | `bandit` | Análisis estático de seguridad |
| CI/CD | GitLab Pipelines | Pipeline de integración continua |
| Diagramas | Markdown / Draw.io | Documentación de arquitectura |
| Licencia | GPL-3.0 | Copyleft — uso educativo obligatorio |

---

## 📦 Installation

> **Requisito previo:** El modo `active` operacional requiere acceso al repositorio
> fuente completo en GitLab. El repositorio público en GitHub contiene únicamente
> la arquitectura sanitizada.

### 1. Clonar el repositorio de laboratorio (GitLab)

```bash
git clone https://gitlab.com/group-cybersecurity-lab/Keylogger.git
cd Keylogger
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar el entorno

Define las variables de entorno para el canal SMTP y el receptor de logs:

```bash
# .env (nunca incluir en el repositorio)
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=lab@example.com
SMTP_PASS=tu_password
SMTP_DEST=investigador@example.com
```

---

## ▶️ Usage

> Todos los modos de uso deben ejecutarse **exclusivamente en entornos de laboratorio
> aislados** (máquinas virtuales sin conexión a redes de producción) y sobre sistemas
> propios o bajo autorización escrita explícita.

### Modo Educativo — Dry Run (por defecto, sin acción real)

```bash
python src/main.py --mode dry-run
```

Simula el ciclo completo del framework sin capturar ni enviar ningún dato real.
Ideal para comprender la arquitectura del sistema de forma segura.

### Modo Simulación — Test

```bash
python src/main.py --mode test
```

Ejecuta el framework con datos de prueba generados internamente, validando
la lógica de captura y el pipeline de exfiltración contra un servidor SMTP local.

### Modo Laboratorio — Active _(solo entorno privado GitLab)_

```bash
python src/main.py --mode active --output logs/sesion_001.log
```

Modo operacional completo. Requiere acceso al repositorio fuente en GitLab
y configuración completa del entorno SMTP de laboratorio.

### Ejecutar análisis de calidad

```bash
# Linting de código
flake8 src/

# Análisis estático de seguridad
bandit -r src/ -o bandit-report.json
```

---

## 📁 Project Structure

```
Keylogger/
│
├── src/                         # Código fuente del framework
│   └── main.py                  # Entry point con control de modos CLI (--mode)
│                                # ⚠️ Componentes operacionales solo en GitLab
│
├── docs/                        # Documentación técnica
│                                # Análisis de vectores, pseudocódigo, RFCs internos
│
├── diagrams/                    # Diagramas de arquitectura y flujo de datos
│                                # Topología de captura → log → exfiltración SMTP
│
├── .gitignore                   # Exclusiones: venv/, logs/, .env, *.log, credenciales
├── LICENSE                      # GNU GPL-3.0 + Aviso legal de uso responsable
└── README.md                    # Documentación principal del proyecto
```

> **Nota sobre la estructura pública:** Las carpetas `tests/`, `configs/` y los
> componentes operacionales de `src/` son **deliberadamente eliminados** del
> repositorio público en GitHub como parte de la estrategia DevSecOps de
> divulgación responsable del laboratorio.

---

## 🔐 Security

### Implicaciones técnicas del vector de captura

Un keylogger opera mediante la intercepción de eventos de entrada del sistema
operativo a nivel de hardware/kernel (hooks de teclado en Windows, listeners de
eventos en Linux). Esto le confiere visibilidad sobre toda la actividad de escritura
del sistema, independientemente de la aplicación activa, lo que lo convierte en un
vector de exfiltración de credenciales de alta criticidad en escenarios de ataque real.

### Canal de exfiltración SMTP

El uso de `smtplib` como mecanismo de exfiltración replica una técnica documentada
en familias de malware de tipo spyware e infostealer. En entornos defensivos, este
tráfico puede detectarse mediante inspección de flujos SMTP salientes no autorizados,
análisis de comportamiento de procesos Python, y reglas de firewall que bloqueen
conexiones a puertos 25/465/587 desde procesos de usuario no esperados.

### Gestión de secretos

El `.gitignore` excluye explícitamente archivos de log (`*.log`), credenciales
SMTP y archivos `.env`, previniendo la exposición accidental de configuraciones
de laboratorio en el repositorio público.

### SAST con Bandit

El pipeline de GitLab ejecuta `bandit` como etapa obligatoria, auditando el
uso de módulos sensibles (`smtplib`, manejo de credenciales en memoria) y
primitivas de riesgo antes de cada merge a la rama principal.

### Uso responsable — Marco legal

El registro de pulsaciones de teclado sin consentimiento explícito del usuario
está tipificado como delito en la mayoría de jurisdicciones bajo leyes de acceso
no autorizado a sistemas informáticos, interceptación de comunicaciones y
violación de privacidad. **Este proyecto debe ejecutarse exclusivamente sobre
sistemas propios o en entornos donde se disponga de autorización escrita previa.**

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura distribuida de doble repositorio, separando
el entorno de investigación activo del portafolio público de forma auditable:

**GitHub** contiene la documentación técnica, diagramas de arquitectura y la
estructura sanitizada del proyecto — orientado a la presentación pública del
portafolio de ciberseguridad.

**GitLab** es el entorno de laboratorio completo y fuente de verdad: contiene
el código fuente operacional íntegro, la suite de tests, las configuraciones
de entorno y el pipeline CI/CD completo (`flake8` → `bandit`).

### 🔗 Full Source Code

👉 Código completo disponible en GitLab:
[https://gitlab.com/group-cybersecurity-lab/Keylogger](https://gitlab.com/group-cybersecurity-lab/Keylogger)

---

## 🚀 Roadmap

Mejoras sugeridas a partir de la arquitectura y stack tecnológico detectados:

- **Cifrado de logs locales** con AES o RSA antes de almacenarlos en disco,
  simulando técnicas de ofuscación de evidencia estudiadas en análisis forense.
- **Canal de exfiltración alternativo** vía HTTPS/Webhook para complementar
  el canal SMTP y estudiar múltiples vectores de exfiltración en paralelo.
- **Tests unitarios con mocks SMTP** (`smtplib.SMTP` mockeado) para validar
  el pipeline de exfiltración sin necesitar un servidor de correo real en CI.
- **Modo de captura acotada por tiempo** (`--duration`) para limitar la
  ventana de captura en sesiones de laboratorio y prevenir acumulación de logs.
- **Rotación automática de archivos de log** por tamaño o tiempo de sesión,
  simulando comportamientos de persistencia observados en APTs reales.
- **Dashboard de análisis de logs** en terminal (TUI con `rich`) para
  visualizar sesiones capturadas con estadísticas de frecuencia de teclas.
- **Detección defensiva integrada** como módulo complementario: reglas para
  identificar keyloggers activos en el sistema, completando la perspectiva
  ofensiva-defensiva del laboratorio.
- **Cobertura pytest ≥ 80%** en la suite de tests del modo `dry-run` y `test`.

---

## 📄 License

Este proyecto está distribuido bajo la licencia
**GNU General Public License v3.0 (GPL-3.0)**.

La GPL-3.0 garantiza las libertades de uso, estudio, distribución y modificación
del software, exigiendo que cualquier trabajo derivado se distribuya bajo los
mismos términos. **El uso con fines maliciosos o en sistemas sin autorización
explícita viola tanto esta licencia como las leyes aplicables.**

📄 [Ver licencia completa](https://github.com/devsebastian44/Keylogger/blob/main/LICENSE)

Copyright © 2025 **Sebastián Zhunaula** (devsebastian44)

---

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <b>Sebastián Zhunaula</b><br/>
      <sub>Security Researcher · Python Developer · Malware Analyst</sub><br/><br/>
      <a href="https://github.com/devsebastian44">
        <img src="https://img.shields.io/badge/GitHub-devsebastian44-black?style=flat&logo=github" />
      </a>
      <br/>
      <a href="https://gitlab.com/group-cybersecurity-lab">
        <img src="https://img.shields.io/badge/GitLab-group--cybersecurity--lab-FC6D26?style=flat&logo=gitlab" />
      </a>
    </td>
  </tr>
</table>

> Este proyecto forma parte de un laboratorio educativo de ciberseguridad orientado
> al estudio de técnicas de ingeniería social, exfiltración de datos y análisis de
> malware de tipo spyware/infostealer, con enfoque estricto en investigación
> defensiva y uso responsable.