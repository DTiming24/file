@echo off
taskkill /f /im Win.exe
timeout /t 5 /nobreak >nul
del "%APPDATA%\Win.exe"
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Win /f
rmdir /s /q "C:\Temp"
del "%~f0"
