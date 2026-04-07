@echo off
echo ================================================
echo    C3 AE Quiz - Deploying Mobile App to the Web
echo ================================================
echo.
echo Welcome! This script will permanently deploy your Mobile App to the internet.
echo We are using "surge.sh", a free and famous hosting provider.
echo.
echo NOTE: Since this is your first time, it will ask for your Email and a Password.
echo When typing your password, the screen will remain blank (for security). Just type it and hit Enter!
echo.
echo Press any key to start the upload...
pause >nul
echo.

:: We use cmd /c because npx might conflict with execution policies in some powershell environments
cd mobile_pwa
cmd.exe /c "npx surge"

echo.
echo ================================================
echo Deployment Complete!
echo You can now open that custom ".surge.sh" link on your cell phone.
echo ================================================
pause
