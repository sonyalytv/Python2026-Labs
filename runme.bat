@echo off
cd /d "%~dp0"

echo ==========================================
echo        Lab08 Setup and Execution
echo ==========================================
echo.

echo [1/4] Setting up the virtual environment...
python -m venv .venv

echo [2/4] Activating the virtual environment...
call .venv\Scripts\activate.bat

echo [3/4] Installing requirements...
pip install -r requirements.txt

echo.
echo [4/4] Running mypy strict type checking...
mypy --strict .
echo.
echo (The above mypy errors, if any, are intentional for the lab)

echo.
echo ==========================================
echo              Running Lab08
echo ==========================================
echo.
python src/lab08.py

echo.
echo ==========================================
echo                Finished!
echo ==========================================
pause