# AI Resume Analyzer

A full-stack application to analyze resumes, extract skills, and calculate a job match score using AI and NLP. The app is built with **React** for the frontend, **Flask** for the backend, and deployed on **AWS EC2** and **Vercel**.

---

## **Features**

1. **Resume Upload**: Accepts resumes in PDF or DOCX format.
2. **Skill Extraction**: Uses NLP to extract key skills from resumes.
3. **Job Match Score**: Calculates a match score between the resume and a job description using cosine similarity.
4. **Responsive UI**: Built with **Material-UI** for an enhanced user experience.
5. **Deployed Backend**: Flask API running on AWS EC2.
6. **Deployed Frontend**: React app hosted on Vercel.

---

## **Tech Stack**

- **Frontend**: React, Material-UI
- **Backend**: Flask, Gunicorn
- **NLP Libraries**: SpaCy, NLTK
- **Deployment**:
  - Backend: AWS EC2
  - Frontend: Vercel

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/somuganesh1/ai-resume-analyzer.git
cd ai-resume-analyzer
```
---

2. Backend Setup (Flask)
Navigate to the resume-parser directory:

```bash
cd resume-parser
```
Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment
pip install flask flask-cors gunicorn pdfminer.six python-docx spacy nltk
python3 -m spacy download en_core_web_sm
```
Run Flask Server
```bash
python app.py
``` 
The backend will run on http://127.0.0.1:5001. 

--- 

3. Frontend Setup (React)
Navigate to the frontend directory:
```bash
cd ../frontend
```
Install Dependencies
```bash
npm install
```
Run React Server
```bash
npm run dev
```
The frontend will run on http://localhost:5173.

---

### **Usage**
1. Visit `http://localhost:5173` in your browser.
2. Upload a resume (PDF/DOCX).
3. Enter a job description in the provided text box.
4. Click **Upload** to analyze the resume and view:
   - Extracted skills.
   - Job match score (%).

---


### **Deployment**

#### **1. Backend Deployment (AWS EC2)**
1. Launch an EC2 Instance:
   - Go to AWS Console → EC2 → Launch Instance.
   - Choose **Ubuntu 22.04** as the OS.
2. Configure the Security Group:
   - Allow **SSH (Port 22)**.
   - Allow **Custom TCP Rule (Port 5001)**.

--- 

Connect to the instance:
```bash
ssh -i resume-key.pem ubuntu@3.142.199.10
```

Set Up Flask API
Upload the backend code to the instance:
```bash
scp -i resume-key.pem -r ./resume-parser ubuntu@3.142.199.10:/home/ubuntu/resume-parser
```

Install Python and dependencies:
```bash
sudo apt update
sudo apt install python3-pip
cd resume-parser
pip3 install flask flask-cors gunicorn pdfminer.six python-docx spacy nltk
python3 -m spacy download en_core_web_sm
```

Start the server with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5001 wsgi:app
```

Flask API is now running on http://3.142.199.10:5001.

---


2. Frontend Deployment (Vercel)
Install Vercel CLI
```bash
npm install -g vercel
```

Deploy Frontend
Navigate to the frontend directory and run:
```bash
vercel --prod
```

React app is now hosted on Vercel.
---
## **API Endpoints**

### **1. Analyze Resume**
- **URL**: `/analyze`
- **Method**: `POST`
- **Request**:
  - **Form data**:
    - `resume`: PDF or DOCX file.
    - `job_description`: Job description text.
---

Project Structure
```bash

ai-resume-analyzer/
│
├── backend/               # Flask Backend
│   ├── app.py             # Main Flask application
│   ├── wsgi.py            # Gunicorn entry point
│   └── uploads/           # Directory for uploaded resumes
│
├── frontend/              # React Frontend
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   └── index.css      # Styling
│   └── public/            # Static assets
│
└── README.md              # Project documentation
```
---
## **Commands Summary**

### **Backend**
- **Install dependencies**: `pip install -r requirements.txt`
- **Run server locally**: `python app.py`
- **Start with Gunicorn**: `gunicorn -w 4 -b 0.0.0.0:5001 wsgi:app`

### **Frontend**
- **Install dependencies**: `npm install`
- **Run locally**: `npm run dev`
- **Deploy to Vercel**: `vercel --prod`

---

## **Future Enhancements**

- **Skill Gap Suggestions**:
  Compare missing skills with job requirements and provide improvement tips.
- **Multi-language Support**:
  Support resumes in multiple languages.
- **Enhanced Analytics**:
  Provide visual insights into resume-job compatibility.



---

Somu Medaka 
