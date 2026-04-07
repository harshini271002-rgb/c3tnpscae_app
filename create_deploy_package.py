import os
import shutil

source_dir = "."
deploy_dir = "Admin_Deploy_Ready"
streamlit_dir = os.path.join(deploy_dir, ".streamlit")

files_needed = [
    "app.py",
    "ai_generator.py",
    "questions_v2.json",
    "requirements.txt",
    "c3_logo.png",
    "app_settings.json",
    "C3_Syllabus.json",
    "student_results.json",
    "students.json"
]

dirs_needed = [
    ".streamlit"
]

print("====================================")
print(" Creating Clean Deployment Package ")
print("====================================")

# Create main dir
if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

# Create sub dirs
if not os.path.exists(streamlit_dir):
    os.makedirs(streamlit_dir)

print(f"Copying files into '{deploy_dir}'...")

# Copy files
for file in files_needed:
    src_path = os.path.join(source_dir, file)
    dst_path = os.path.join(deploy_dir, file)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f" -> Copied {file}")
    else:
        # Create empty placeholder if some json files don't exist yet but are required
        if file.endswith('.json'):
            with open(dst_path, 'w') as f:
                if 'settings' in file:
                    f.write('{"pw": "admin", "q_limit": 25}')
                else:
                    f.write('[]')
            print(f" -> Created blank placeholder for {file}")
        else:
            print(f" -> WARNING: {file} not found!")

# Copy static directories carefully
for d in dirs_needed:
    src_path = os.path.join(source_dir, d)
    dst_path = os.path.join(deploy_dir, d)
    if os.path.exists(src_path):
        for item in os.listdir(src_path):
            s = os.path.join(src_path, item)
            d_item = os.path.join(dst_path, item)
            if os.path.isfile(s):
                shutil.copy2(s, d_item)
                print(f" -> Copied {d}/{item}")

print("\nSUCCESS! Your clean deployment folder is ready.")
print(f"Folder Location: {os.path.abspath(deploy_dir)}")
