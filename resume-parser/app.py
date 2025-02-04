from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pdfminer.high_level
import docx
import spacy
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download stopwords if not already available
nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)
CORS(app)

nlp = spacy.load("en_core_web_sm")  # Load NLP model

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return pdfminer.high_level.extract_text(pdf_path)

# Function to extract text from Word documents
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract key skills from resume text
def extract_skills(text):
    doc = nlp(text.lower())  # Process text with Spacy
    skill_keywords = ["python", "java", "c++", "machine learning", "deep learning",
                      "flask", "django", "react", "angular", "azure", "aws", "linux",
                      "docker", "kubernetes", "sql", "nosql", "nlp", "cloud computing"]

    extracted_skills = [token.text for token in doc if token.text in skill_keywords]
    return list(set(extracted_skills))  # Remove duplicates

# Function to calculate job match score
def calculate_match_score(resume_text, job_description):
    vectorizer = CountVectorizer().fit_transform([resume_text, job_description])
    vectors = vectorizer.toarray()
    similarity_score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(similarity_score * 100, 2)  # Convert to percentage

# Resume Analysis Endpoint
@app.route("/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files or "job_description" not in request.form:
        return jsonify({"error": "Resume and job description required"}), 400

    file = request.files["resume"]
    job_description = request.form["job_description"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text based on file type
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    skills = extract_skills(text)
    match_score = calculate_match_score(text, job_description)

    return jsonify({
        "message": "Resume analyzed successfully",
        "filename": file.filename,
        "match_score": match_score,
        "extracted_skills": skills
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)