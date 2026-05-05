from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def find_skills(text):
    skills = ["python", "java", "c++", "html", "css", "javascript"]
    found = []
    for skill in skills:
        if skill in text:
            found.append(skill)
    return found

@app.route("/", methods=["GET", "POST"])
def index():
    skills = []
    if request.method == "POST":
        file = request.files["resume"]
        text = extract_text(file)
        skills = find_skills(text)
    return render_template("index.html", skills=skills)

if __name__ == "__main__":
    app.run(debug=True)