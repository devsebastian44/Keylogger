# 🛡️ Sentinel Framework: Educational Keylogger & Research Tool

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Repository-orange?logo=gitlab)
![License](https://img.shields.io/badge/License-GPL--3.0-red)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Educational](https://img.shields.io/badge/Purpose-Educational%20Only-blue)
![Warning](https://img.shields.io/badge/⚠-Authorized%20Use%20Only-red)

Este proyecto es un **Framework de Ciberseguridad Educativa** diseñado para demostrar los principios de captura de eventos, persistencia y exfiltración de datos en entornos controlados de laboratorio.

> [!IMPORTANT]
> **DISCLAIMER ÉTICO:** Este software ha sido desarrollado exclusivamente con fines educativos y de investigación. El uso de esta herramienta contra objetivos sin consentimiento previo es ilegal y poco ético. El autor no se hace responsable del mal uso de este código.

---

## 🏗️ Arquitectura del Sistema

El proyecto sigue una estructura modular y escalable pensada para entornos DevSecOps profesonales:

| Carpeta | Propósito |
| :--- | :--- |
| `src/` | Núcleo del framework y lógica de captura. |
| `tests/` | Pruebas de integración y simulación de comportamiento. |
| `docs/` | Documentación técnica detallada y políticas de ética. |
| `diagrams/` | Visualización de flujos de datos y arquitectura. |
| `configs/` | Archivos de configuración y dependencias. |

---

## 🔒 Estrategia de Seguridad (GitHub vs GitLab)

Este repositorio utiliza una estrategia de **Diferenciación de Entornos**:

- **GitHub (Portafolio):** Escaparate profesional. Contiene estructura, documentación, diagramas y pseudocódigo educativo. Demuestra mejores prácticas DevSecOps sin funcionalidades críticas.
- **GitLab (Laboratorio Público):** Laboratorio educativo completo. Contiene implementación funcional, payloads activos, tests automatizados y pipeline CI/CD con análisis SAST. Accesible públicamente para investigación.

---

## 🚀 Instalación y Acceso

> [!IMPORTANT]
> El repositorio completo con todo el código funcional está disponible en **GitLab** para acceso completo.

https://gitlab.com/group-cybersecurity-lab/Keylogger-lab.git

## 🛠️ Modo de Uso

El framework se controla mediante argumentos desde la terminal:

```bash
# Modo Educativo (Seguro / Dry Run) - Por defecto
python src/main.py --mode dry-run

# Modo Simulación (Test)
python src/main.py --mode test

# Modo Laboratorio (Activo) - Requiere acceso privado
python src/main.py --mode active --output logs/sesion_001.log
```

| Argumento | Descripción |
| :--- | :--- |
| `--mode` | Selecciona el modo: `dry-run`, `active` o `test`. |
| `--output` | Especifica la ruta de salida para los logs (solo en modo `active`). |

---

## 🏗️ Pipeline DevSecOps

El proyecto integra un flujo de trabajo automatizado en GitLab Cielo:

- **Linting:** Validación de estándares de código.
- **SAST:** Escaneo de vulnerabilidades con `bandit`.
- **Unit Testing:** Validación de módulos con `pytest`.

---

## 📝 Documentación Adicional

- [Guía de Ética y Legalidad](docs/ethics.md)
- [Arquitectura Detallada](docs/architecture.md)
- [Diagramas de Flujo](diagrams/data_flow.md)