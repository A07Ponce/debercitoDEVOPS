# Mi Paquete ALISSON

# mi-paquete — CI/CD práctico hasta la construcción del PACKAGE

Este repositorio es un **ejemplo completo** que demuestra un ciclo de CI/CD con **GitHub Actions** que:

- Ejecuta pruebas (`pytest`)
- Construye un paquete Python (`sdist` y `wheel`)
- Publica el paquete como **artefacto** de la ejecución de Actions

## Estructura del proyecto

## Objetivo del pipeline (CI)

1. Al hacer `push` o abrir `pull request` en `main`, GitHub Actions ejecuta:

   - Instalación de dependencias
   - Ejecución de pruebas (`pytest`)
   - Construcción del paquete (`python -m build`)
   - Subida de `dist/*` como artefacto

2. Si los tests fallan, la build se marca como fallida y no se genera artefacto.

## Ejecución local (rápida)

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install pytest build
pytest -q

# construir
python -m build --sdist --wheel
ls dist/
```
