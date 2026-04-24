@echo off
echo ==========================================
echo         Lab07 Setup and Execution
echo ==========================================
echo.

echo [1/4] Setting up the virtual environment...
python -m venv .venv

echo [2/4] Activating the virtual environment...
call .venv\Scripts\activate.bat

echo [3/4] Installing requirements...
:: Note: This will show an error if requirements.txt doesn't exist yet!
pip install -r requirements.txt

echo.
echo [4/4] Running mypy strict type checking...
mypy --strict src/lab07.py
echo The above errors are intentional, see the lab below...

echo.
echo ==========================================
echo              Running Lab07
echo ==========================================
echo.
python src/lab07.py

echo.
echo ==========================================
echo                Finished!
echo ==========================================
pause