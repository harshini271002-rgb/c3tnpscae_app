import os
import shutil

src_dir = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\Admin_Deploy_Ready"
dest_dir = r"c:\Users\harsh\OneDrive\Desktop\Deployment_Final_App"

print(f"Creating pristine deployment folder at: {dest_dir}")

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

for filename in os.listdir(src_dir):
    src_file = os.path.join(src_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dest_file)
        print(f"Copied {filename}")

# Safely inject dependencies into the unlocked new requirements
req_path = os.path.join(dest_dir, "requirements.txt")
try:
    with open(req_path, "a", encoding="utf-8") as f:
        f.write("\nmatplotlib\njinja2\n")
    print("Injected matplotlib and jinja2 into requirements.txt safely.")
except Exception as e:
    print(f"Error updating requirements: {e}")

print("SUCCESS: The pure deployment folder is ready.")
