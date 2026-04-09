import os
import shutil

src_main = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz"
src_deploy = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\Admin_Deploy_Ready"
dest_dir = r"c:\Users\harsh\OneDrive\Desktop\TNPSC_Cloud_Upload_Ready_v2"

print(f"Creating brand new pristine upload folder at: {dest_dir}")

# Remove existing if present to ensure clean state
if os.path.exists(dest_dir):
    try:
        shutil.rmtree(dest_dir)
    except:
        pass

try:
    os.makedirs(dest_dir)
except:
    pass

# We take the perfectly merged 'app.py' and 'theme_config' from our previous clean environment
files_from_deploy = ["app.py", "theme_config.toml"]
for f in files_from_deploy:
    shutil.copy2(os.path.join(src_deploy, f), os.path.join(dest_dir, f))
    print(f"Copied base logic structure -> {f}")

# We take the absolute latest live data directly from the main folder!
data_files = [
    "questions_v2.json", 
    "app_settings.json", 
    "C3_Syllabus.json", 
    "students.json", 
    "student_results.json",
    "c3_logo.png"
]
for f in data_files:
    path = os.path.join(src_main, f)
    if os.path.exists(path):
        shutil.copy2(path, os.path.join(dest_dir, f))
        print(f"Copied latest live user data -> {f}")
    else:
        print(f"WARNING: Missing data file {f} in {src_main}")

# Strictly create perfect requirements.txt
req_content = """streamlit==1.52.2
pandas
google-generativeai>=0.8.3
Pillow
plotly
matplotlib
jinja2
"""
req_path = os.path.join(dest_dir, "requirements.txt")
with open(req_path, "w", encoding="utf-8") as rf:
    rf.write(req_content)
print("Created perfect requirements.txt!")

print("\nSUCCESS! Folder is perfectly packed and awaiting GitHub upload.")
