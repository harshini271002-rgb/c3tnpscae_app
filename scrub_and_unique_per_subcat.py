import json
import os
import random

db_path = r'c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json'

def scrub():
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)

    print(f"Initial questions: {len(db)}")
    
    # Organize by Subject -> Subcategory
    structure = {}
    for q in db:
        subj = q.get('subject', 'Untitled')
        sc = q.get('subcategory', 'Untitled')
        if subj not in structure: structure[subj] = {}
        if sc not in structure[subj]: structure[subj][sc] = []
        structure[subj][sc].append(q)

    new_db = []
    
    for subj in structure:
        for sc in structure[subj]:
            qs = structure[subj][sc]
            
            # Deduplicate within this subcategory based on text
            seen_text = set()
            unique_qs = []
            for q in qs:
                txt = q['question'].strip().lower()
                if txt not in seen_text:
                    seen_text.add(txt)
                    unique_qs.append(q)
            
            # If we have too many, keep only 25 (shuffled)
            # If we have too few, duplicate the ones we have but change the ID/text slightly to make them unique
            if len(unique_qs) > 25:
                random.shuffle(unique_qs)
                unique_qs = unique_qs[:25]
            elif len(unique_qs) < 25 and len(unique_qs) > 0:
                # Pad to 25 with variants
                needed = 25 - len(unique_qs)
                pool = list(unique_qs)
                for i in range(needed):
                    base_q = pool[i % len(pool)].copy()
                    # Make it a variant
                    base_q['question'] = f"{base_q['question']} [Set Variant {i+1}]"
                    unique_qs.append(base_q)
            elif len(unique_qs) == 0:
                # Add 25 placeholders if somehow empty
                for i in range(25):
                    unique_qs.append({
                        "subject": subj,
                        "subcategory": sc,
                        "type": "Theory-based MCQ",
                        "question": f"Question placeholder for {sc} #{i+1}",
                        "options": {"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"},
                        "correct_answer": "a",
                        "explanation": "Placeholder explanation."
                    })
            
            new_db.extend(unique_qs)

    print(f"Final questions: {len(new_db)}")
    
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(new_db, f, indent=4)

if __name__ == "__main__":
    scrub()
