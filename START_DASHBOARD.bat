@echo off
cd /d "%~dp0"
py -m pip show pandas >nul 2>nul || py -m pip install pandas openpyxl
py server.py
pause
