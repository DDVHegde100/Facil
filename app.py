from flask import Flask, request, render_template, jsonify
from summarizer import summarize_text
from question_generator import generate_questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    content = request.json.get('content', '')
    summary = summarize_text(content)
    return jsonify({'summary': summary})

@app.route('/generate_questions', methods=['POST'])
def generate():
    content = request.json.get('content', '')
    questions = generate_questions(content)
    return jsonify({'questions': questions})

if __name__ == "__main__":
    app.run(debug=True)
