@echo off
echo ██████╗      ██╗    ██╗  ██╗ ██████╗ ██████╗ ███████╗
echo ██╔══██╗     ██║    ██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝
echo ██║  ██║     ██║    █████╔╝ ██║   ██║██████╔╝█████╗  
echo ██║  ██║██   ██║    ██╔═██╗ ██║   ██║██╔══██╗██╔══╝  
echo ██████╔╝╚█████╔╝    ██║  ██╗╚██████╔╝██║  ██║███████╗
echo  ╚═════╝  ╚════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
echo.

echo [1/4] Activando entorno virtual...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)

echo [2/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo [3/4] Navegando al proyecto Django...
cd chatbot_dj_project

echo [4/4] Iniciando servidor Django...
echo.
echo ========================================
echo  SERVIDOR INICIADO EN: http://127.0.0.1:8000/
echo  Presiona Ctrl+C para detener el servidor
echo ========================================
echo.
python manage.py runserver

echo.
echo Servidor detenido.
pause