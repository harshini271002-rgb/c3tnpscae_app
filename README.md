# C³ Institute — TNPSC AE Quiz App

## How to Run (Windows)
1. Double-click `START_APP.bat`
2. Browser opens automatically at http://localhost:8501

## Login Credentials
- **Student Login**: Enter your Name + Student ID
- **Admin Password**: `c3admin2024`

## Folder Contents
| File | Purpose |
|------|---------|
| `app.py` | Main application |
| `questions_v2.json` | Question database (4900+ questions) |
| `student_results.json` | Student quiz result records |
| `app_settings.json` | Timer and global settings |
| `requirements.txt` | Python dependencies |
| `START_APP.bat` | One-click Windows launcher |
| `.streamlit/config.toml` | Theme configuration |
| `c3_logo.png` | Institute logo |

## Manual Start
```
pip install -r requirements.txt
streamlit run app.py
```

## Online Deployment
Deploy free at: https://streamlit.io/cloud
- Upload all files from this folder
- Set `app.py` as the main file
