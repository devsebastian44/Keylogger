# ⌨️ Keylogger — Framework de Captura de Keystrokes en Python

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/Exfiltración-SMTP%20%2F%20smtplib-orange?style=flat&logo=gmail&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![SAST](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![Platform](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux-0078D6?style=flat&logo=windows&logoColor=white)


> ⚠️ **AVISO LEGAL Y ÉTICO:** Este proyecto es de uso **estrictamente educativo y para
> investigación en ciberseguridad defensiva**. Su ejecución en sistemas, dispositivos o
> redes sin la autorización explícita del propietario es **ilegal y constituye un delito**.
> El autor no se responsabiliza por ningún uso indebido de este software fuera de
> entornos controlados y autorizados. — _Extracto del LICENSE (GPL-3.0)_

---

## 🧠 Descripción General

Este proyecto es un **framework de captura de pulsaciones de teclado (keylogger)** desarrollado en Python 3.9+, orientado a laboratorios de investigación en ciberseguridad, análisis de ingeniería social y comprensión de vectores de exfiltración de datos en entornos controlados.

El sistema utiliza un **sistema de modos de operación** CLI que permite simular comportamientos de exfiltración vía **SMTP**, replicando técnicas utilizadas por amenazas avanzadas (APT) para el estudio de medidas defensivas.

---

## ⚙️ Características

- **Modos de Ejecución CLI:** `dry-run` (seguro), `test` (simulación) y `active`.
- **Captura de Eventos:** Intercepción de keystrokes en tiempo real mediante APIs del SO.
- **Exfiltración SMTP:** Canal de envío automatizado de logs a servidores de laboratorio.
- **Control de Calidad:** Integración con `flake8` (linting) y `bandit` (seguridad).
- **Arquitectura Modular:** Separación clara entre motor, ejemplos y documentación.

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnología | Propósito |
|---|---|---|
| Lenguaje | Python 3.9+ | Lógica principal del framework |
| Captura | `pynput` / `keyboard` | Intercepción de eventos de teclado |
| Exfiltración | `smtplib` | Envío de datos vía correo SMTP |
| CI/CD | GitHub Actions | Pipeline automatizado de calidad |
| SAST | `bandit` | Análisis estático de seguridad |
| Pruebas | `pytest` | Suite de tests funcionales |

---

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/devsebastian44/Keylogger.git
cd Keylogger
```

### 2. Entorno Virtual
```bash
# Crear y activar
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 3. Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración
Copia el archivo de ejemplo y configura tus credenciales de laboratorio:
```bash
cp .env.example .env
```

---

## ▶️ Uso

### Modo Educativo (Dry Run)
```bash
python src/main.py --mode dry-run
```
Simula el flujo completo sin capturar datos reales.

### Modo Simulación (Test)
```bash
python src/main.py --mode test
```
Ejecuta el framework con eventos inyectados de forma interna.

### Modo Laboratorio (Active)
```bash
python src/main.py --mode active --output logs/sesion.log
```
Ejecución operacional completa (requiere configuración SMTP).

---

## 🧪 Pruebas y Calidad

Para asegurar la integridad del código, puedes ejecutar las siguientes herramientas:

**Ejecutar Tests:**
```bash
pytest
```

**Análisis de Seguridad:**
```bash
bandit -r src/
```

**Validación de Estilo:**
```bash
flake8 .
```

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Sigue estos pasos para colaborar:

1. Haz un **Fork** del proyecto.
2. Crea una rama para tu mejora (`git checkout -b feature/NuevaMejora`).
3. Realiza tus cambios siguiendo los [Conventional Commits](https://www.conventionalcommits.org/).
4. Envía un **Pull Request** para revisión.

---

## 📁 Estructura del Proyecto

```
Keylogger/
├── src/                 # Lógica principal y entry point
├── tests/               # Pruebas automatizadas (Mocks)
├── docs/                # Documentación técnica y ética
├── diagrams/            # Diagramas de arquitectura
├── .github/workflows/   # Pipeline de CI/CD
└── requirements.txt     # Dependencias del proyecto
```

---

## 📄 Licencia

Distribuido bajo la licencia **GNU GPL-3.0**. Ver `LICENSE` para más detalles.

Copyright © 2025 **Sebastián Zhunaula** (devsebastian44)