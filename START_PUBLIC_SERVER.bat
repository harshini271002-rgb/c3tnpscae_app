@echo off
echo ========================================================
echo    C3 AE Quiz - Starting Public Web Server
echo ========================================================
echo.
echo Starting the Admin Dashboard...
start /B python -m streamlit run app.py --server.port 8501 --server.headless true

echo.
echo Please wait while we generate your Public Internet Link...
echo (You may need to hit Enter if it pauses)
timeout /t 5 >nul

echo.
echo ========================================================
echo YOUR PUBLIC SECURE LINK IS GENERATING BELOW:
echo ========================================================
echo.
:: Run localtunnel targeting port 8501
npx localtunnel --port 8501
