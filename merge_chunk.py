import json

DB_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json"
CHUNK_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\unit3_t1.json"
SUBJECT = "Engineering Mechanics & Strength of Materials"
SUBCAT = "Forces: Types & Laws"

try:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception:
    db = []

with open(CHUNK_FILE, "r", encoding="utf-8") as f:
    chunk_qs = json.load(f)

# Clear old placeholders for THIS subtopic in THIS subject
db = [q for q in db if not (q.get("subject") == SUBJECT and q.get("subcategory") == SUBCAT and q.get("question", "").startswith("Sample placeholder"))]

db.extend(chunk_qs)

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4)

print(f"Merged {len(chunk_qs)} questions for {SUBCAT} into main DB.")
