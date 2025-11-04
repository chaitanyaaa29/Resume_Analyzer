from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

app = Flask(__name__)

# Predefined job skills (you can expand this list)
SKILLS = ["python", "java", "c++", "html", "css", "javascript",
          "flask", "django", "react", "sql", "machine learning", "ai", "data analysis"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['resume_text']

    # --- Text cleaning ---
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [w for w in tokens if w not in stop_words and w not in string.punctuation]

    # --- Word frequency ---
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # --- Skill extraction ---
    found_skills = [skill for skill in SKILLS if skill in text]

    # --- Job readiness score ---
    readiness = min(100, len(found_skills) * 10)

    top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

    return render_template('result.html',
                           top_words=top_words,
                           found_skills=found_skills,
                           readiness=readiness,
                           total_words=len(words))

if __name__ == "__main__":
    app.run(debug=True)
