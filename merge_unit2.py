import json
import os

DB_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json"
NEW_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\unit2_generated.json"

try:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception:
    db = []

try:
    with open(NEW_FILE, "r", encoding="utf-8") as f:
        new_qs = json.load(f)
except Exception as e:
    print(f"Error reading new file: {e}")
    exit(1)

# Remove placeholders for the subcategories we are injecting
new_subcats = set([q["subcategory"] for q in new_qs])
db = [q for q in db if not (q.get("subject") == "Engineering Mechanics & Strength of Materials" and q.get("subcategory") in new_subcats and q.get("question").startswith("Sample placeholder"))]

db.extend(new_qs)

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4)

print(f"Successfully merged {len(new_qs)} new questions into the database!")
