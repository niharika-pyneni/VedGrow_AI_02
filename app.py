from flask import Flask, request, render_template_string
import json
import webbrowser
from threading import Timer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load FAQ data
with open("faq_data.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )[0]

    best_match = similarity_scores.argmax()

    if similarity_scores[best_match] < 0.2:
        return (
            "Sorry, I couldn't find a relevant answer. Please try asking your question differently.",
            []
        )

    sorted_indices = similarity_scores.argsort()[::-1]

    related_questions = []

    for idx in sorted_indices:
        if idx != best_match:
            related_questions.append(questions[idx])

        if len(related_questions) == 4:
            break

    return answers[best_match], related_questions

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>StudyBuddy AI</title>

    <style>

        body{
            margin:0;
            font-family:Arial, sans-serif;
            background:#eef2f7;
            display:flex;
            justify-content:center;
            align-items:center;
            min-height:100vh;
            padding:20px;
        }
        
        .container{
    width:900px;
    max-width:95%;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 5px 20px rgba(0,0,0,0.15);
        }

        h1{
            text-align:center;
            color:#2c3e50;
            margin-bottom:10px;
        }

        .subtitle{
            text-align:center;
            color:#666;
            margin-bottom:25px;
        }

        form{
            display:flex;
            gap:10px;
        }

        input{
            flex:1;
            padding:12px;
            border-radius:8px;
            border:1px solid #ccc;
            font-size:15px;
        }

        button.ask-btn{
            background:#3498db;
            color:white;
            border:none;
            padding:12px 20px;
            border-radius:8px;
            cursor:pointer;
        }

        button.ask-btn:hover{
            background:#2980b9;
        }

        .faq-section{
            margin-top:25px;
        }

        .faq-section h3{
            color:#2c3e50;
        }

        .faq-btn{
            background:#f1f5f9;
            border:none;
            padding:10px;
            margin:5px;
            border-radius:8px;
            cursor:pointer;
        }

        .faq-btn:hover{
            background:#dbeafe;
        }

        .chat-box{
            margin-top:25px;
        }

        .user-msg{
            background:#dbeafe;
            padding:12px;
            border-radius:10px;
            margin-bottom:10px;
        }

        .bot-msg{
            background:#ecfdf5;
            padding:12px;
            border-radius:10px;
        }

        .related-box{
    margin-top:20px;
    padding:15px;
    background:#fff8e7;
    border-radius:10px;
    border:1px solid #f5d98b;
        }

.related-box h3{
    margin-top:0;
    color:#2c3e50;
}

.related-question{
    background:white;
    padding:10px;
    margin:8px 0;
    border-radius:8px;
    border:1px solid #ddd;
    cursor:pointer;
    transition:0.2s;
}

.related-question:hover{
    background:#f9fafb;
}

.footer{
    margin-top:25px;
    text-align:center;
    color:#777;
    font-size:13px;
}

    </style>

    <script>
        function fillQuestion(question){
        document.getElementById("questionInput").value = question;
        document.getElementById("questionInput").focus();
        }
    </script>

</head>

<body>

<div class="container">

    <h1>📚 StudyBuddy AI</h1>

    <div class="subtitle">
        Your AI-Powered Study Assistant
    </div>

    <form method="POST">
        <input
            id="questionInput"
            type="text"
            name="question"
            placeholder="Ask a study-related question..."
            required
        >

        <button class="ask-btn" type="submit">
            Ask
        </button>
    </form>

    <div class="faq-section">
        <h3>📌 Popular Questions</h3>

        <button class="faq-btn"
        onclick="fillQuestion('How can I improve my concentration while studying?')">
        Improve concentration
        </button>

        <button class="faq-btn"
        onclick="fillQuestion('What is the Pomodoro Technique?')">
        Pomodoro Technique
        </button>

        <button class="faq-btn"
        onclick="fillQuestion('How can I avoid procrastination?')">
        Avoid procrastination
        </button>

        <button class="faq-btn"
        onclick="fillQuestion('How do I prepare for exams effectively?')">
        Exam preparation
        </button>

        <button class="faq-btn"
        onclick="fillQuestion('What is active recall?')">
        Active Recall
        </button>

        <button class="faq-btn"
        onclick="fillQuestion('How can I reduce exam anxiety?')">
        Exam anxiety
        </button>

    </div>

    {% if answer %}

<div class="chat-box">

    <div class="user-msg">
        <strong>You Asked:</strong><br>
        {{ question }}
    </div>

    <div class="bot-msg">
        <strong>StudyBuddy AI:</strong><br>
        {{ answer }}
    </div>

</div>

<div class="related-box">

    <h3>📚 You may also want to ask</h3>

    {% for q in related_questions %}

    <div
    class="related-question"
    onclick="fillQuestion('{{ q }}')"
>
    {{ q }}
</div>

    {% endfor %}

</div>

{% endif %}

    <div class="footer">
        Powered by NLP (TF-IDF + Cosine Similarity)
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    answer = None
    question = ""
    related_questions = []

    if request.method == "POST":
        question = request.form["question"]

        answer, related_questions = get_answer(question)

    return render_template_string(
        HTML,
        answer=answer,
        question=question,
        related_questions=related_questions
    )


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)