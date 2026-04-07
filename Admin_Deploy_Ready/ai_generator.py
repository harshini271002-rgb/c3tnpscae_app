import google.generativeai as genai
import json
import os
import re

# IMPORTANT: You must configure the API key in the environment or directly here.
# Currently assuming an environment variable for security
GENAI_API_KEY = os.environ.get("GEMINI_API_KEY", "") 

if GENAI_API_KEY:
    genai.configure(api_key=GENAI_API_KEY)

def generate_questions_from_src(src_path, subject, unit, topic, subtopic, num_questions=5, dynamic_api_key=None):
    """
    Source-grounded Question Generation (NotebookLM Style)
    Strictly follows content flow of provided handwritten notes/PDFs.
    """
    active_key = dynamic_api_key.strip() if dynamic_api_key and dynamic_api_key.strip() else GENAI_API_KEY
    if not active_key:
        return {"error": "Google Gemini API key required for Source-Grounded Generation."}
        
    try:
        genai.configure(api_key=active_key)
        
        # Decide content part (PDF vs Image)
        is_pdf = src_path.lower().endswith('.pdf')
        if is_pdf:
            content_part = genai.upload_file(path=src_path)
            # Wait for the file to be processed (crucial for large PDFs)
            import time
            while content_part.state.name == "PROCESSING":
                time.sleep(2)
                content_part = genai.get_file(content_part.name)
            if content_part.state.name == "FAILED":
                return {"error": "PDF processing failed on Google servers."}
        else:
            from PIL import Image
            content_part = Image.open(src_path)
        
        # Use gemini-1.5-flash as default (fast and reliable)
        model_name = 'gemini-1.5-flash'
        model = genai.GenerativeModel(model_name)
        
        system_instruction = f"""
        You are a prestigious TNPSC AE (Civil Engineering) Exam Setter.
        BEHAVIOR: You act like Google NotebookLM—completely source-grounded.
        
        SOURCE MATERIAL: You are analyzing handwritten notes/PDFs for:
        Unit: {unit} 
        Topic: {topic}
        Subtopic: {subtopic}
        
        STRICT RULES:
        1. Generate exactly {num_questions} questions.
        2. SOURCE-BOUND: Every question MUST be derivable from the provided document. If the document is insufficient, return "Insufficient source material".
        3. CONTENT FLOW: Follow the logical progression of the handwritten notes.
        4. LEVEL: Moderate to Hard (Assistant Engineer Standard).
        5. ANTI-HALLUCINATION: Do not use external knowledge or general engineering facts if not mentioned or implied by formulas in the notes.
        6. NO DUPLICATES: Every question must be distinct.
        7. MATH NOTATION: Use actual Greek symbols (σ, τ, ε, θ, π, ϕ, Δ, λ) and math symbols (√, ±, ≠, ≤, ≥, ÷, ×) instead of writing them out as words like "sigma" or "root".
        """
        
        prompt = f"""
        Produce a balanced mix of these Question Types from the source:
        1. Theory-based MCQ
        2. Numerical / Problem-based (Show steps in explanation)
        3. Assertion–Reason (A: ..., R: ...)
        4. Match the Following (P,Q,R vs 1,2,3)
        5. Statement Combination (Select i, ii only, etc.)
        6. Diagram-based (Ask about specific symbols/sketches in the notes)

        OUTPUT SCHEMA (STRICT JSON ARRAY):
        [
            {{
                "questionText": "Full text of the question",
                "options": {{"a": "...", "b": "...", "c": "...", "d": "..."}},
                "correctAnswer": "a", 
                "detailedExplanation": "Cite relevant section from notes + full calculation steps if numerical.",
                "questionType": "Numerical",
                "difficultyLevel": "Hard",
                "diagramReference": "Mention specific sketch found in notes or 'None'",
                "unitTag": "{unit}",
                "topicTag": "{topic}",
                "subtopicTag": "{subtopic}"
            }}
        ]

        Return RAW JSON ONLY. No markdown wrappers.
        """
        
        response = model.generate_content([system_instruction, content_part, prompt])
        raw_text = response.text.strip()
        
        # Safety check for "Insufficient source material"
        if "Insufficient source material" in raw_text:
            return {"error": "The uploaded document does not contain enough information to generate questions for this subtopic."}

        # Robust JSON cleaning
        clean_text = re.sub(r'```json\s*|```', '', raw_text)
        json_data = json.loads(clean_text)
        
        return {"success": True, "questions": json_data}
        
    except Exception as e:
        return {"error": str(e)}

def generate_from_text_content(text_content, subject, subtopic, num_questions=25, dynamic_api_key=None):
    """
    Generates MCQs strictly from pasted Notebook LLM text content.
    """
    active_key = dynamic_api_key.strip() if dynamic_api_key and dynamic_api_key.strip() else GENAI_API_KEY
    if not active_key:
        return {"error": "Google Gemini API key required for AI Generation."}
        
    if not text_content or len(text_content.strip()) < 100:
        return {"error": "Content box is empty or too short. Please paste the Notebook LLM content."}

    try:
        genai.configure(api_key=active_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        system_msg = f"""
        You are a high-fidelity Question Extractor and Generator for TNPSC AE civil engineering exams.
        
        INPUT ANALYSIS:
        The text below contains content from Notebook LLM. It could be raw study notes OR a list of pre-written MCQs.
        
        YOUR MISSION:
        1. **STRICT EXTRACTION**: If the text already has questions using labels like "Question Text:", "Options:", "Correct Answer:", and "Detailed Explanation:", you MUST extract them exactly as written.
        2. **STRICT GENERATION**: If the text is raw notes, generate exactly {num_questions} new MCQs.
        
        TECHNICAL CONTEXT:
        Subject: {subject}, Subtopic: {subtopic}
        
        SYMBOLS RULE: Always use actual Unicode symbols (σ, ε, τ, θ, π, √, ≤, ≥, Δ) instead of writing "sigma", "epsilon", "tau", etc.
        
        TEXT SOURCE:
        {text_content}
        """
        
        prompt = """
        Output JSON in this structure:
        [
            {
                "question": "Question text",
                "options": {"a": "...", "b": "...", "c": "...", "d": "..."},
                "correct_answer": "a", 
                "explanation": "Reasoning...",
                "type": "Theory-based MCQ"
            }
        ]
        Return RAW JSON only.
        """
        
        response = model.generate_content([system_msg, prompt])
        raw_text = response.text.strip()
        
        # Clean JSON
        clean_text = re.sub(r'```json\s*|```', '', raw_text)
        json_data = json.loads(clean_text)
        
        # Add tags 
        for q in json_data:
            q["subject"] = subject
            q["subcategory"] = subtopic
            
        return {"success": True, "questions": json_data}
        
    except Exception as e:
        return {"error": str(e)}

def local_smart_extract(text_content, subject, subtopic):
    """
    Version 9.0: Enhanced Assertion-Reason & Match-the-Following Splitter.
    Solves the bug where "Assertion (A)" blocked the discovery of real options.
    Removes newline restriction on "Options:" divider.
    """
    import re
    questions = []
    # Normalize ALL line endings including single \r
    text_content = text_content.replace('\r\n', '\n').replace('\r', '\n')
    
    # 1. SPLIT INTO QUESTION BLOCKS (More lenient: Digit + space is enough)
    blocks = re.split(r'(?:\n|^)\s*\d+[.\)]?\s+', text_content)
    
    for block in blocks:
        block = block.strip()
        if not block or len(block) < 30: continue
        
        try:
            # Anchor detection (More flexible - can be middle of line)
            a_marker = re.search(r'\n\s*(?:Correct Answer|Correct|Ans|Key):', block, re.IGNORECASE)
            e_marker = re.search(r'\n\s*(?:Detailed Explanation|Explanation|Exp|Reasoning):', block, re.IGNORECASE)
            o_marker = re.search(r'\s*Options:', block, re.IGNORECASE)

            # --- Q-TEXT vs OPTIONS CORE SPLIT ---
            ans_start_root = a_marker.start() if a_marker else (e_marker.start() if e_marker else len(block))
            
            q_text = block
            opts_part = ""

            if o_marker:
                q_text = block[:o_marker.start()].strip()
                opts_part = block[o_marker.end():ans_start_root].strip()
            else:
                # Fallback: Find the first (a) marker. Optimized to find markers at start of line or after space.
                markers = list(re.finditer(r'(?:\n|\s|^)[(\[]?[aA][.\)\]]\s*', block))
                valid_a = None
                for m in markers:
                    # Ignore if surrounded by common non-option words
                    lb = block[max(0, m.start()-20) : m.start()].lower()
                    if any(k in lb for k in ["assertion", "statement", "list", "table", "group"]):
                        continue
                    valid_a = m
                    break
                
                if valid_a:
                    q_text = block[:valid_a.start()].strip()
                    opts_part = block[valid_a.start():ans_start_root].strip()

            # Final cleanup of Q_TEXT
            q_text = re.sub(r'^(?:Question\s*Text:\s*|Result:\s*)', '', q_text, flags=re.IGNORECASE).strip()
            q_text = re.sub(r'Options:\s*$', '', q_text, flags=re.IGNORECASE).strip()

            # --- OPTION PARSING (High-Precision Chronological Discovery) ---
            options = {"a": "Not found", "b": "Not found", "c": "Not found", "d": "Not found"}
            if opts_part:
                clean_opts_blob = re.sub(r'(?:Correct Answer|Correct|Ans|Key):.*$', '', opts_part, flags=re.IGNORECASE | re.DOTALL).strip()
                
                # Find ALL potential marker candidates (Lighter requirement on spaces)
                marker_pats = r'[(\[]?([a-dA-D])[.\)\]]\s*'
                all_matches = list(re.finditer(marker_pats, clean_opts_blob))
                
                # SEQUENCE-LOCKING: Force markers to appear in 'a -> b -> c -> d' order.
                # This prevents 'A.' at the end of 'explanation of A.' from stealing the A slot.
                valid_seq = []
                current_search_pos = 0
                for letter_goal in ['a', 'b', 'c', 'd']:
                    target = None
                    for m in all_matches:
                        if m.group(1).lower() == letter_goal and m.start() >= current_search_pos:
                            target = m
                            break
                    if target:
                        valid_seq.append(target)
                        current_search_pos = target.end()

                # Content Extraction based on Locked sequence
                for i in range(len(valid_seq)):
                    m = valid_seq[i]
                    letter = m.group(1).lower()
                    start_idx = m.end()
                    end_idx = valid_seq[i+1].start() if i+1 < len(valid_seq) else len(clean_opts_blob)
                    
                    if letter in options:
                        options[letter] = clean_opts_blob[start_idx:end_idx].strip()

            # --- ANSWER & EXPLANATION ---
            correct_ans = "a"
            if a_marker:
                ans_text = block[a_marker.end() : (e_marker.start() if e_marker else len(block))].strip()
                ltr = re.search(r'[a-dA-D]', ans_text, re.IGNORECASE)
                if ltr: correct_ans = ltr.group(0).lower()
                
            explanation = "Extracted from source content."
            if e_marker:
                explanation = block[e_marker.end():].strip()
            
            if all(v == "Not found" for v in options.values()): continue

            questions.append({
                "question": q_text,
                "options": options,
                "correct_answer": correct_ans,
                "explanation": explanation,
                "type": "Theory-based MCQ",
                "subject": subject,
                "subcategory": subtopic
            })
            
        except Exception:
            continue
            
    return {"success": True, "questions": questions}

if __name__ == "__main__":
    print("AI Question Generator initialized.")
