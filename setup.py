import subprocess
import sys

def install_requirements():
    print("Installing requirements from requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_nltk_data():
    print("Downloading NLTK data...")
    # Import inside function to ensure it's available after install_requirements
    import nltk
    # Essential resources for the preprocessor
    resources = ['punkt', 'stopwords', 'wordnet', 'omw-1.4', 'punkt_tab']
    for resource in resources:
        try:
            nltk.download(resource, quiet=True)
            print(f"Downloaded {resource}")
        except Exception as e:
            print(f"Failed to download {resource}: {e}")

def download_spacy_model():
    print("Downloading Spacy model 'en_core_web_sm'...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

if __name__ == "__main__":
    try:
        install_requirements()
        download_nltk_data()
        download_spacy_model()
        print("\nSetup complete! You can now run 'python app.py'")
    except Exception as e:
        print(f"\nAn error occurred during setup: {e}")
