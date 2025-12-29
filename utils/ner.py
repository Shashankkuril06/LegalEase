import spacy

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback or need to download
    print("SpaCy model 'en_core_web_sm' not found. Please run 'python -m spacy download en_core_web_sm'")
    nlp = None

def get_entities(text):
    """Extracts named entities using spaCy."""
    if not nlp:
        return {}
        
    doc = nlp(text)
    entities = {
        "ORG": [],
        "PERSON": [],
        "DATE": [],
        "GPE": [] # Geopolitical Entity suitable for 'Jurisdiction' context sometimes
    }
    
    for ent in doc.ents:
        if ent.label_ in entities:
            if ent.text not in entities[ent.label_]:
                entities[ent.label_].append(ent.text)
                
    return entities
