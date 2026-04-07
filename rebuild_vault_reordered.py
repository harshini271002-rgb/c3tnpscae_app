import json
import os
import shutil

DB_FILE = "questions_v2.json"
VAULT_DIR = "MASTER_VAULT"

def sync_to_physical_vault(questions):
    base_dir = VAULT_DIR
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    
    # Group by Subject/Subcategory
    grouped = {}
    for q in questions:
        key = (q.get("subject", "Uncategorized"), q.get("subcategory", "Uncategorized"))
        if key not in grouped: grouped[key] = []
        grouped[key].append(q)
    
    for (subj, subcat), qs in grouped.items():
        # Sanitize names
        s_subj = "".join([c if c.isalnum() or c in " _-" else "_" for c in subj])
        s_subcat = "".join([c if c.isalnum() or c in " _-" else "_" for c in subcat])
        
        target_dir = os.path.join(base_dir, s_subj, s_subcat)
        if not os.path.exists(target_dir): os.makedirs(target_dir)
        
        with open(os.path.join(target_dir, "published_questions.json"), "w", encoding="utf-8") as f:
            json.dump(qs, f, indent=4)

if __name__ == "__main__":
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            db = json.load(f)
        sync_to_physical_vault(db)
        print("Vault rebuilt successfully from rectified database.")
    else:
        print("DB not found.")
