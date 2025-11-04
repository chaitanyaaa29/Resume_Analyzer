# Resume_Analyzer
AI-Powered Resume Analyzer: A Flask web app that analyzes resume text using NLTK to extract skills, find key keywords, and generate a job-readiness score — helping users quickly gauge how optimized their resumes are for job applications.

AI-Powered Resume Analyzer
🚀 Features

📝 Paste your resume text directly into the app

🔍 Uses NLTK for keyword and skill extraction

🧩 Detects key technical and soft skills from a predefined list

📊 Generates a “Job Readiness Score” based on skills found

📑 Displays top 10 keywords and total word count

🎨 Clean, minimal web interface built with HTML, CSS, and Flask templates

🛠️ Tech Stack

Frontend: HTML, CSS
Backend: Python (Flask)
NLP: NLTK
Database: None (lightweight single-file app)

📁 Folder Structure
ResumeAnalyzer/
│
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── result.html
⚙️ Installation
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Then open a Python shell and run:

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

Run the app:

python app.py

Visit http://127.0.0.1:5000/ in your browser.

💡 How It Works

User pastes resume text.

NLTK tokenizes and cleans it.

The app finds matching skills and frequent words.

Generates a readiness score (0–100).

Displays insights neatly on a result page.

🌟 Future Enhancements

PDF/DOCX upload with auto-text extraction

Resume-to-job-description similarity matching

Word cloud visualization and live deployment
