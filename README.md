# ⌨️ Keylogger — Sentinel Framework

![CI Pipeline](https://github.com/devsebastian44/Keylogger/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python&logoColor=white)
![SAST](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)

> [!IMPORTANT]
> **This project is for educational and ethical cybersecurity purposes only.**
> Any use of this software on systems without explicit authorization is illegal.

Sentinel is an educational framework designed to study keystroke capture techniques and data exfiltration vectors. It is optimized for research in controlled laboratory environments.

---

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/devsebastian44/Keylogger.git
cd Keylogger

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Copy the example environment file and adjust your settings:
```bash
cp .env.example .env
```

### 3. Running the Project
The framework supports multiple execution modes:

- **Educational (Dry Run):**
  ```bash
  python src/main.py --mode dry-run
  ```
- **Test Simulation:**
  ```bash
  python src/main.py --mode test
  ```
- **Active Lab (Requires installation of all dependencies):**
  ```bash
  python src/main.py --mode active --output logs/session.log
  ```

---

## 🧪 Testing & Quality
We maintain high standards through automated testing and security scanning.

**Run tests:**
```bash
pytest
```

**Run Linting:**
```bash
flake8 .
```

**Run Security Scan:**
```bash
bandit -r src/
```

---

## 📁 Project Structure
- `src/`: Core logic and entry point.
- `tests/`: Automated functional tests (uses mocks).
- `configs/`: Example configurations and settings.
- `docs/`: Technical documentation and ethical guidelines.
- `diagrams/`: Architectural diagrams.

---

## 🤝 Contributing
Contributions are welcome! Follow these steps:

1. **Fork** the project.
2. Create a **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit** your changes using [Conventional Commits](https://www.conventionalcommits.org/).
4. **Push** to the branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## 📄 License
Distributed under the **GNU GPL-3.0 License**. See `LICENSE` for more information.

Copyright © 2025 **Sebastián Zhunaula** (devsebastian44)