import PyPDF2
import docx

def extract_text_from_pdf(filepath):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
    return text

def extract_text_from_docx(filepath):
    """Extracts text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(filepath)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
    return text

def read_file(filepath):
    """Reads a file based on its extension."""
    if filepath.lower().endswith('.pdf'):
        return extract_text_from_pdf(filepath)
    elif filepath.lower().endswith('.docx'):
        return extract_text_from_docx(filepath)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
