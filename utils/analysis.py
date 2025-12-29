from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessor import clean_text, get_sentences
import numpy as np

def extract_keywords(text, top_n=10):
    """Extracts top N keywords using TF-IDF."""
    if not text or not text.strip():
        return []
    
    # We treat the text as a single document for keyword extraction relative to itself 
    # (or we could split into sentences to find words important in this doc).
    # Standard TF-IDF requires a corpus. Here we can treat sentences as documents 
    # to find words that are unique/important in specific sentences vs others, 
    # OR we can just use simple frequency count if it's a single doc.
    # However, to use sklearn's TFidf as requested:
    
    sentences = get_sentences(text)
    if not sentences:
        return []
        
    cleaned_sentences = [clean_text(s) for s in sentences]
    
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)
        feature_names = vectorizer.get_feature_names_out()
        
        # Sum tfidf scores for each word across all sentences
        dense = tfidf_matrix.todense()
        # Sum columns (words)
        episode = dense.sum(axis=0) 
        # Convert to flat list
        episode_list = episode.tolist()[0]
        
        # Pair words with scores
        phrase_scores = [pair for pair in zip(range(0, len(episode_list)), episode_list) if pair[1] > 0]
        
        # Sort by score desc
        sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
        
        # Get top N
        top_indices = [i[0] for i in sorted_phrase_scores[:top_n]]
        keywords = [feature_names[i] for i in top_indices]
        
        return keywords
    except ValueError:
        # Handle empty vocabulary or other sklearn errors
        return []

def summarize_text(text, top_n=3):
    """Extractive summarization using sentence scoring based on TF-IDF."""
    sentences = get_sentences(text)
    if len(sentences) <= top_n:
        return text
    
    cleaned_sentences = [clean_text(s) for s in sentences]
    
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)
        
        # Score sentences by summing their word TF-IDF scores
        # tfidf_matrix is (n_sentences, n_features)
        sentence_scores = tfidf_matrix.sum(axis=1) # Sum of row
        
        # Get top N sentence indices
        # argsort returns indices that would sort the array, extract last top_n
        top_sentence_indices = np.argsort(sentence_scores, axis=0)[-top_n:]
        top_sentence_indices = top_sentence_indices.flatten().tolist()[0] # numpy matrix to list
        if isinstance(top_sentence_indices, int): # Handle single item case
             top_sentence_indices = [top_sentence_indices]
        
        # Sort indices to keep original order
        top_sentence_indices.sort()
        
        summary = " ".join([sentences[i] for i in top_sentence_indices])
        return summary
        
    except ValueError:
        # Fallback if TF-IDF fails (e.g. empty text)
        return " ".join(sentences[:top_n])
