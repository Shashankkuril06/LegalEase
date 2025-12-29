# LegalEase ⚖️

LegalEase is a NLP-powered tool designed to simplify legal documents for non-legal users. It analyzes PDF or DOCX files to extract key clauses, identify important terms, and provide a concise extractive summary.

## 🎯 Project Goal
- Extract text from PDF/DOCX.
- Identify standard legal clauses (Termination, Confidentiality, Indemnity, etc.) using Regex.
- Generate an **extractive summary** using TF-IDF scoring.
- Highlight key legal terms and named entities (Dates, Organizations, Parties).

## 🛠️ Tech Stack
- **Language:** Python
- **Backend:** Flask
- **NLP Libraries:**
    - `NLTK`: Tokenization, Stopword removal, Lemmatization.
    - `spaCy`: Named Entity Recognition (NER).
    - `scikit-learn`: TF-IDF for keyword extraction and sentence scoring.
    - `re`: Regular expressions for clause detection.
- **File Handling:** `PyPDF2`, `python-docx`.

## 🚀 How to Run

1. **Clone/Navigate to the directory**:
   ```bash
   cd LegalEase
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Usage**:
   - Open browser at `http://127.0.0.1:5000`
   - Upload a legal PDF or DOCX.
   - View the Analysis Result.

## 📂 Project Structure
```
LegalEase/
├── app.py                 # Flask App Entry Point
├── requirements.txt       # Dependencies
├── test_core.py           # Script to test NLP logic without UI
├── static/
│   └── style.css          # UI Styling
├── templates/
│   ├── index.html         # Upload Page
│   └── result.html        # Results Page
└── utils/
    ├── file_handler.py    # PDF/DOCX reading
    ├── preprocessor.py    # Cleaning & Tokenization
    ├── clause_detector.py # Regex Clause Logic
    ├── analysis.py        # TF-IDF & Summarization
    └── ner.py             # Entity Extraction
```

---
*Disclaimer: LegalEase is for educational purposes and does not provide professional legal advice. Always consult a qualified attorney.*
