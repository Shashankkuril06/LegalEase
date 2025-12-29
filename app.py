from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from utils.file_handler import read_file
from utils.clause_detector import detect_clauses
from utils.analysis import extract_keywords, summarize_text
from utils.ner import get_entities

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # 1. Extract Text
            text = read_file(filepath)
            
            # 2. Pipeline
            clauses = detect_clauses(text)
            keywords = extract_keywords(text)
            summary = summarize_text(text)
            entities = get_entities(text)
            
            # Cleanup
            os.remove(filepath)
            
            return render_template('result.html', 
                                   summary=summary, 
                                   clauses=clauses, 
                                   keywords=keywords, 
                                   entities=entities)
            
        except Exception as e:
            return f"An error occurred: {str(e)}"
            
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
