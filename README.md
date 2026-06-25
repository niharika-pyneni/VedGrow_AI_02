# 📚 StudyBuddy AI - FAQ Chatbot

## 📖 Overview

StudyBuddy AI is an NLP-powered FAQ chatbot developed as part of **VedGrow AI Internship - Task 02**.

The chatbot helps students by answering frequently asked questions related to study techniques, exam preparation, concentration, revision methods, time management, active recall, and productivity.

The system uses Natural Language Processing (NLP) to identify and return the most relevant answer from a predefined FAQ dataset.

---

## 🚀 Features

- Study-related FAQ assistance
- NLP-based question matching
- TF-IDF Vectorization
- Cosine Similarity Matching
- Related Question Recommendations
- Interactive Web Interface
- Automatic Browser Launch
- User-Friendly Design

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- Natural Language Processing (NLP)

---

## ⚙️ Working Principle

1. User enters a study-related question.
2. The question is converted into numerical vectors using TF-IDF Vectorization.
3. Cosine Similarity compares the user's query with stored FAQ questions.
4. The chatbot retrieves the most relevant answer.
5. Related questions are recommended to help users explore similar topics.

---

## 📂 Project Structure

```text
VedGrow_AI_02/
│
├── app.py
├── faq_data.json
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/niharika-pyneni/VedGrow_AI_02.git
```

### Navigate to Project Folder

```bash
cd VedGrow_AI_02
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

The application will automatically open in your browser at:

```text
http://127.0.0.1:5000
```

---

## 🔮 Future Enhancements

- Voice-based interaction
- Dark mode support
- Larger FAQ dataset
- Chat history support
- Advanced AI-based responses

---

