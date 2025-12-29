import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

# NLTK resources should be downloaded in setup, but we import here.
# Ensure 'punkt', 'stopwords', 'wordnet' are available.

def clean_text(text):
    """Lowers text and removes special characters/punctuation."""
    text = text.lower()
    # Remove special chars but keep spaces and alphanumeric
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def preprocess_text(text):
    """Full preprocessing pipeline: clean -> remove stopwords -> lemmatize."""
    # 1. Clean
    cleaned = clean_text(text)
    
    # 2. Tokenize
    tokens = word_tokenize(cleaned)
    
    # 3. Stopword Removal
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # 4. Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    
    return " ".join(lemmatized)

def get_sentences(text):
    """Returns list of sentences from raw text."""
    return sent_tokenize(text)
