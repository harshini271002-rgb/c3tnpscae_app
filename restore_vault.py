import json
import os

DB_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json"
VAULT_DIR = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\MASTER_VAULT"

def restore_from_vault():
    if not os.path.exists(VAULT_DIR):
        print("Vault not found.")
        return
    
    # Load current DB
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            db = json.load(f)
    else:
        db = []
    
    print(f"Current DB size: {len(db)}")
    
    # Track existing questions by text + subcategory to avoid duplicates
    existing_fingerprints = set()
    for q in db:
        fingerprint = (q.get("question", "").strip().lower(), q.get("subcategory", "").lower())
        existing_fingerprints.add(fingerprint)
    
    new_adds = 0
    # Walk the vault
    for root, dirs, files in os.walk(VAULT_DIR):
        if "published_questions.json" in files:
            vault_file = os.path.join(root, "published_questions.json")
            with open(vault_file, 'r', encoding='utf-8') as f:
                try:
                    vault_qs = json.load(f)
                    for q in vault_qs:
                        fingerprint = (q.get("question", "").strip().lower(), q.get("subcategory", "").lower())
                        if fingerprint not in existing_fingerprints:
                            db.append(q)
                            existing_fingerprints.add(fingerprint)
                            new_adds += 1
                except:
                    print(f"Error reading {vault_file}")
    
    print(f"Added {new_adds} questions from vault.")
    print(f"Post-recovery DB size: {len(db)}")
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4)

if __name__ == "__main__":
    restore_from_vault()
