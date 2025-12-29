import re

CLAUSE_PATTERNS = {
    "Termination": r"(termination|terminate|cancel|end of agreement|term of agreement)",
    "Confidentiality": r"(confidentiality|confidential|non-disclosure|secrecy)",
    "Indemnity": r"(indemnity|indemnify|hold harmless|defend)",
    "Jurisdiction": r"(jurisdiction|governing law|laws of|venue|courts of)",
    "Liability": r"(liability|liable|damages|limitation of liability)",
    "Payment Terms": r"(payment|compensation|fees|invoice|reimbursement)",
    "Force Majeure": r"(force majeure|act of god|beyond reasonable control)"
}

def detect_clauses(text):
    """Scans text for clause keywords using Regex."""
    detected = []
    text_lower = text.lower()
    
    for clause, pattern in CLAUSE_PATTERNS.items():
        if re.search(pattern, text_lower):
            detected.append(clause)
            
    return detected
