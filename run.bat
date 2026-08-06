@echo off
REM Double-click this file to start the HR Copilot app.
REM It launches the Streamlit server; then open http://localhost:8501 in your browser.
cd /d "%~dp0"
set PYTHONUTF8=1
".venv\Scripts\streamlit.exe" run app.py
