import os
import json
import fitz
import google.generativeai as genai

print("="*60)
print("   C³ Institute - AI Unit 2 MCQ Generator")
print("="*60)

GENAI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if not GENAI_API_KEY:
    GENAI_API_KEY = input("\n🔑 Please enter your GEMINI_API_KEY: ").strip()

if not GENAI_API_KEY:
    print("FATAL: GEMINI_API_KEY missing. Exiting.")
    exit(1)

genai.configure(api_key=GENAI_API_KEY)

unit2_pdf = r"c:\Users\harsh\OneDrive\Desktop\AE\unit2-EM & SoM Final.pdf"
yct_pdf = r"c:\Users\harsh\OneDrive\Desktop\AE\YCT Civil AE 1.pdf"
output_file = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\unit2_generated.json"

print("\n📚 Extracting sample style from YCT Question Bank (Please wait)...")
yct_style_text = ""
try:
    doc_yct = fitz.open(yct_pdf)
    for idx in range(10, min(30, len(doc_yct))):
        yct_style_text += doc_yct[idx].get_text() + "\n"
    doc_yct.close()
except Exception as e:
    print("Warning: Could not read YCT PDF fully:", e)

print(f"📄 Extracting content from Unit 2 PDF...")
unit2_text = ""
try:
    doc_u2 = fitz.open(unit2_pdf)
    for idx in range(0, min(60, len(doc_u2))):
        unit2_text += doc_u2[idx].get_text() + "\n"
    doc_u2.close()
except Exception as e:
    print("Error reading Unit 2 PDF:", e)
    exit(1)

print("\n🤖 Synthesizing 20 high-quality MCQs using Gemini 1.5 Pro...")
print("This may take 30-60 seconds depending on API response time...")

model = genai.GenerativeModel('gemini-1.5-pro')

prompt = f"""
You are an expert TNPSC Civil Engineering Exam Question Setter. 
I am providing you with the core material for "Unit II: Engineering Mechanics and Strength of Materials" (see Content Section).
I am also providing you with a sample of the expected question style from the YCT Question Bank (see Style Section).

Task: Generate a highly realistic, mixed question set of exactly 20 MCQs based STRICTLY on the Unit 2 content provided.

REQUIRED MCQ QUESTION TYPES (Mix these evenly):
1. Theory-based MCQ
2. Numerical / Problem-based
3. Assertion–Reason
4. Match the Following
5. Statement Combination
6. Diagram-based (Simulate by asking about standard diagrams like BMD/SFD shapes)

Format Requirements:
Output strictly as a JSON array of objects. No markdown formatting like ```json.
Each object must have the following keys exactly:
- "subject": "Engineering Mechanics & Strength of Materials"
- "subcategory": (Choose one of: "Forces: Types & Laws", "CoG & MI", "Friction", "Stresses and Strains", "Beams: SFD & BMD", "Theory of simple bending", "Deflection of beams", "Torsion", "Combined stresses", "Stress Transformations & Failure Theories", "Analysis of plane trusses")
- "type": (One of the 6 types exactly as listed above)
- "question": "The question text itself"
- "options": {{"a": "...", "b": "...", "c": "...", "d": "..."}}
- "correct_answer": "a", "b", "c", or "d"
- "explanation": "Detailed step-by-step or theoretical explanation."
- "difficulty": "Hard" or "Medium"

### STYLE SECTION (YCT Sample)
{yct_style_text[:2000]}

### CONTENT SECTION (Unit 2 Source)
{unit2_text[:40000]}
"""

try:
    response = model.generate_content(prompt)
    raw_text = response.text.strip()
    
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    if raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
        
    data = json.loads(raw_text.strip())
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print(f"\n✅ SUCCESS! Generated {len(data)} questions and saved to {output_file}")
    print("You can now ask your AI Assistant to merge these into the main database.")
    input("Press Enter to exit...")
except Exception as e:
    print("\n❌ Error generating questions:", e)
    input("Press Enter to exit...")
