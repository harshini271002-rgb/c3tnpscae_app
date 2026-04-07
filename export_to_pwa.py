import json
import base64
import os
import shutil

src_json = "questions_v2.json"
pwa_dir = "mobile_pwa"
dest_json = os.path.join(pwa_dir, "data.json")

def process_image(path):
    # Already web link or base64
    if not path: return None
    if path.startswith("http") or path.startswith("data:"): 
        return path
        
    # Check local path
    target = path
    if not os.path.isabs(path):
        target = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        
    if os.path.exists(target):
        try:
            ext = os.path.splitext(target)[1].lower().replace('.', '')
            if not ext: ext = "png"
            with open(target, "rb") as img_file:
                b64 = base64.b64encode(img_file.read()).decode('utf-8')
                return f"data:image/{ext};base64,{b64}"
        except Exception:
            return None
    return None

print("=============================================")
print(" Mobile PWA Exporter - Offline Data compiler ")
print("=============================================")

if not os.path.exists(pwa_dir):
    os.makedirs(pwa_dir)

print(f"1. Loading Admin Database ({src_json})...")
try:
    with open(src_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading questions: {e}")
    exit()

print("2. Packaging embedded images into Base64 for Offline Caching...")
converted_images = 0
for q in data:
    if q.get('imageUrl'):
        b64 = process_image(q['imageUrl'])
        if b64 and b64 != q['imageUrl']:
            q['imageUrl'] = b64
            converted_images += 1

print(f"3. Writing {len(data)} questions directly to {dest_json}...")
with open(dest_json, 'w', encoding='utf-8') as f:
    json.dump(data, f)
    
print("4. Securing App Icon...")
icon_src = "c3_logo.png"
if os.path.exists(icon_src):
    try:
        from PIL import Image
        img = Image.open(icon_src)
        img = img.resize((512, 512)) # standardize PWA icon size
        img.save(os.path.join(pwa_dir, "icon.png"))
        print(" -> Converted c3_logo.png to Mobile Icon format.")
    except Exception:
        shutil.copy(icon_src, os.path.join(pwa_dir, "icon.png"))
        print(" -> Copied raw logo as icon.")
else:
    print(" -> Warning: c3_logo.png not found for App Icon.")

print("\nSUCCESS! The 'mobile_pwa' folder is now fully baked.")
print("How to deploy:")
print("1. Upload the entire 'mobile_pwa' folder to a free host like GitHub Pages, Vercel, or Netlify.")
print("2. Open the URL on your mobile phone browser.")
print("3. Tap 'Add to Home Screen'.")
print("4. Done! It will now work 100% Offline like a native app.")
