from flask import Flask, request, render_template
from summarizer import generate_summary
from question_generator import generate_questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    questions = []

    if request.method == "POST":
        input_text = request.form["input_text"]
        summary = generate_summary(input_text)
        questions = generate_questions(input_text)

    return render_template("index.html", summary=summary, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
