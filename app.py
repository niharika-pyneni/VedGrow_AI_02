from flask import Flask, request, render_template_string, session
import webbrowser
import os
import markdown
from threading import Timer

from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)
load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in .env file")
app.secret_key = os.getenv("SECRET_KEY")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def get_answer(user_question):

    system_prompt = """
You are StudyBuddy AI, a helpful AI-powered study assistant.

Your job is to answer ONLY questions related to:
- School and college subjects
- Exams
- Study techniques
- Productivity
- Learning strategies
- Career guidance

If the user asks anything unrelated (movies, politics, sports, celebrities, romance, etc.), politely reply:

"Sorry, I can only assist with study-related questions."

Keep your answers concise, friendly and easy to read.

Formatting Rules:
- Use short paragraphs.
- Use bullet points whenever possible.
- Do not write one huge paragraph.
- Leave a blank line between sections.
- Keep every answer visually clean.
"""

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    # Last 5 conversations
    for chat in session.get("history", []):
        messages.append({
            "role": "user",
            "content": chat["question"]
        })
        messages.append({
            "role": "assistant",
            "content": chat["answer"]
        })

    messages.append({
        "role": "user",
        "content": user_question
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4,
            max_tokens=250
    )

        ai_answer = markdown.markdown(
            response.choices[0].message.content
        )

    except Exception:
        ai_answer = "Sorry, something went wrong while contacting the AI. Please try again."
    return ai_answer

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>StudyBuddy AI</title>

<style>
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:#f3f4f6;
}

.chat-container{
    width:900px;
    max-width:95%;
    margin:25px auto;
    background:white;
    border-radius:18px;
    overflow:hidden;
    box-shadow:0 5px 20px rgba(0,0,0,.15);
}

.chat-header{
    background:#2563eb;
    color:white;
    padding:18px 25px;
    font-size:22px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.status{
    font-size:13px;
    color:#dbeafe;
}

.chat-area{
    height:75vh;
    overflow-y:auto;
    padding:25px;
    background:#eef2f7;
    display:flex;
    flex-direction:column;
}

form{
    display:flex;
    gap:10px;
    margin-top:auto;
    padding-top:20px;
}

input{
    flex:1;
    padding:14px;
    border-radius:25px;
    border:1px solid #ccc;
    font-size:15px;
}

.ask-btn{
    background:#2563eb;
    color:white;
    border:none;
    border-radius:25px;
    padding:14px 24px;
    cursor:pointer;
}

.user-msg{
    background:#2563eb;
    color:white;
    width:fit-content;
    max-width:70%;
    padding:14px;
    margin:15px 0 10px auto;
    border-radius:18px 18px 4px 18px;
}

.bot-msg{
    background:white;
    width:fit-content;
    max-width:70%;
    padding:14px;
    margin:10px 0;
    border-radius:18px 18px 18px 4px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
    white-space:pre-wrap;
    line-height:1.6;
}

.chat-box{
    display:flex;
    flex-direction:column;
    margin:15px 0;
}

.faq-btn{
    margin:5px;
    padding:10px 14px;
    border:none;
    border-radius:20px;
    background:#dbeafe;
    cursor:pointer;
}


.footer{
    text-align:center;
    padding:20px;
    color:#666;
}
</style>

<script>
function fillQuestion(question){
document.getElementById("questionInput").value = question;
}
window.onload = function () {
    document.getElementById("questionInput").focus();
}
</script>

</head>


<body>

<div class="chat-container">

<div class="chat-header">
    🤖 <strong>StudyBuddy AI</strong>
    <span class="status">● Online • Powered by Groq</span>
</div>

<div class="chat-area">


<h3>📌 Popular Questions</h3>


<button class="faq-btn" onclick="fillQuestion('How can I improve my concentration while studying?')">
Improve concentration
</button>

<button class="faq-btn" onclick="fillQuestion('What is the Pomodoro Technique?')">
Pomodoro Technique
</button>

<button class="faq-btn"
onclick="fillQuestion('How do I prepare for exams effectively?')">
Exam Preparation
</button>

<button class="faq-btn"
onclick="fillQuestion('What is active recall?')">
Active Recall
</button>

<button class="faq-btn" onclick="fillQuestion('How can I avoid procrastination?')">
Avoid procrastination
</button>


{% for chat in session.get("history", [])|reverse %}

<div class="chat-box">

<div class="user-msg">
<strong>You:</strong><br>
{{chat.question}}
</div>


<div class="bot-msg">
<strong>StudyBuddy AI:</strong><br>
{{chat.answer|safe}}
</div>


</div>

{% endfor %}


<form method="POST">

<input
id="questionInput"
type="text"
name="question"
placeholder="Type your study question here..."
required>

<button class="ask-btn" type="submit">
Ask
</button>

</form>

<div class="footer">
Powered by Groq • Llama 3.3 70B
</div>


</div>

</div>

</body>
</html>
"""



@app.route("/", methods=["GET", "POST"])
def home():

    answer = None
    question = ""

    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        question = request.form["question"]

        answer = get_answer(question)
        session["history"].append({
            "question": question,
            "answer": answer
        })

        session["history"] = session["history"][-5:]
    return render_template_string(
    HTML,
    answer=answer,
    question=question
)


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)