# rewrite_history.ps1
$ref = "1d6b1e1"
git checkout --orphan main-clean
git reset --hard

# Commit 1: Repository Structure
git checkout $ref -- .gitignore LICENSE README.md
git add .
git commit -m "feat: initial repository structure and documentation"

# Commit 2: Architectural Guidelines
git checkout $ref -- docs/ diagrams/
git add .
git commit -m "docs: add project architecture and ethical guidelines"

# Commit 3: Core Logic
git checkout $ref -- src/__init__.py src/main.py src/core/examples.py src/core/__init__.py
git add .
git commit -m "feat: implement core main logic and examples"

# Commit 4: Advanced Engine and Testing
git checkout $ref -- src/core/engine.py tests/
git add .
git commit -m "feat: implement advanced engine and testing suite"

# Commit 5: CI/CD
git checkout $ref -- .gitlab-ci.yml
git add .
git commit -m "ci: add gitlab-ci pipeline configuration"

# Commit 6: Support Infrastructure
git checkout $ref -- configs/ scripts/
git add .
git commit -m "chore: add configuration files and publishing scripts"

# Commit 7: Final Refinement
git checkout $ref -- .
git add .
git commit -m "fix(scripts): optimize engine filtering for public release"
