@echo off
echo ================================================
echo    C3 Institute TNPSC AE Quiz App - Starting...
echo ================================================

:: Install dependencies if needed
pip install -r requirements.txt --quiet

:: Start the app
echo Opening app at http://localhost:8501
start http://localhost:8501
streamlit run app.py --server.port 8501

pause
