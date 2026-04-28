# =============================================================================
# scripts/publish_public.ps1 - VERSIÓN OPTIMIZADA (GitHub)
# Mantenimiento de Portafolio: Limpieza y Publicación en GitHub
# =============================================================================

Write-Host "[*] Iniciando limpieza y actualización de Keylogger para GitHub..." -ForegroundColor Cyan

# 1. Validaciones Iniciales
$currentBranch = git rev-parse --abbrev-ref HEAD
if ($currentBranch -ne "main") {
    Write-Host "[!] Error: Debes estar en 'main' para actualizar el portafolio." -ForegroundColor Red
    exit
}

if (git status --porcelain) {
    Write-Host "[!] Tienes cambios sin guardar. Haz commit antes de continuar." -ForegroundColor Yellow
    exit
}

# 2. Limpieza Local Previa
Write-Host "[*] Limpiando archivos temporales y logs..." -ForegroundColor Yellow
Remove-Item -Path "*.log", "*.rules", "iptables_backup_*" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "__pycache__", ".pytest_cache" -Recurse -Force -ErrorAction SilentlyContinue

# 3. Estrategia de Rama de Publicación (Sanitización)
Write-Host "[*] Preparando rama de publicación 'public'..."
git checkout -B public main

# 4. Filtrado de Archivos (Seguridad DevSecOps)
Write-Host "[*] Aplicando filtros de seguridad para el portafolio público..." -ForegroundColor Cyan
# Eliminamos componentes sensibles o internos para el portafolio público
git rm -r --cached tests/ -f 2>$null
git rm -r --cached configs/ -f 2>$null
git rm -r --cached scripts/ -f 2>$null
git rm --cached src/core/engine.py -f 2>$null

# 5. Commit de Lanzamiento y Actualización en GitHub
git commit -m "docs: update public portfolio (sanitized)" --allow-empty
Write-Host "[*] Actualizando GitHub (origin)..." -ForegroundColor Green
git push origin public:main --force

# 6. Retorno Seguro
Write-Host "[*] Volviendo a la rama principal..."
git checkout main -f
git clean -fd 2>$null

Write-Host "[*] Portafolio en GitHub actualizado correctamente." -ForegroundColor Green
