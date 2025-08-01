@echo off
echo ========================================
echo   INSTALACION INICIAL - DJ KORE CHATBOT
echo ========================================
echo.

echo [1/3] Creando entorno virtual...
python -m venv .venv
if errorlevel 1 (
    echo ERROR: No se pudo crear el entorno virtual
    echo Asegurate de tener Python instalado
    pause
    exit /b 1
)

echo [2/3] Activando entorno virtual...
call .venv\Scripts\activate.bat

echo [3/3] Instalando dependencias...
pip install -r requirements.txt

echo.
echo ========================================
echo   INSTALACION COMPLETADA!
echo   Ejecuta 'start.bat' para iniciar el servidor
echo ========================================
pause