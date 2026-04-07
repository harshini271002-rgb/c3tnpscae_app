import json
import sys

# Usage: python merge_macro.py <json_file_path> <Subcategory Name>

if len(sys.argv) < 3:
    print("Usage: python merge_macro.py <json_file_path> <Subcat>")
    exit(1)

CHUNK_FILE = sys.argv[1]
SUBCAT = sys.argv[2]
DB_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json"
SUBJECT = "Engineering Mechanics & Strength of Materials"

try:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception:
    db = []

try:
    with open(CHUNK_FILE, "r", encoding="utf-8") as f:
        chunk_qs = json.load(f)
except Exception as e:
    print(f"Failed to read {CHUNK_FILE}: {e}")
    exit(1)

# Clear old placeholders for THIS subtopic in THIS subject
db = [q for q in db if not (q.get("subject") == SUBJECT and q.get("subcategory") == SUBCAT and q.get("question", "").startswith("Sample placeholder"))]

db.extend(chunk_qs)

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4)

print(f"Merged {len(chunk_qs)} natively-generated questions for '{SUBCAT}' into main DB.")
