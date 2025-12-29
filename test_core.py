from utils.file_handler import extract_text_from_pdf
from utils.preprocessor import clean_text, preprocess_text
from utils.clause_detector import detect_clauses
from utils.analysis import extract_keywords, summarize_text
from utils.ner import get_entities

SAMPLE_TEXT = """
AGREEMENT
This Non-Disclosure Agreement (the "Agreement") is entered into by and between Acme Corp ("Disclosing Party") and John Doe ("Receiving Party") as of January 1, 2024.

1. Confidentiality
The Receiving Party agrees not to disclose any Confidential Information to third parties.

2. Termination
This Agreement shall terminate exactly 2 years from the date hereof.

3. Jurisdiction
This Agreement shall be governed by the laws of the State of California.

4. Indemnity
Receiving Party agrees to indemnify Disclosing Party.
"""

def test_pipeline():
    print("--- RAW TEXT ---")
    print(SAMPLE_TEXT.strip())
    
    print("\n--- DETECTED CLAUSES ---")
    clauses = detect_clauses(SAMPLE_TEXT)
    print(clauses)
    
    print("\n--- ENTITIES ---")
    entities = get_entities(SAMPLE_TEXT)
    print(entities)
    
    print("\n--- KEYWORDS ---")
    keywords = extract_keywords(SAMPLE_TEXT)
    print(keywords)
    
    print("\n--- SUMMARY ---")
    summary = summarize_text(SAMPLE_TEXT, top_n=2)
    print(summary)

if __name__ == "__main__":
    test_pipeline()
