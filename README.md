# StudyBuddy AI 📚🤖

StudyBuddy AI is an AI-powered FAQ chatbot designed to help students with study-related questions. It uses Natural Language Processing (NLP) techniques to understand user queries and provide relevant answers from a predefined FAQ knowledge base.

The chatbot uses TF-IDF Vectorization and Cosine Similarity to match user questions with the most relevant answers and provide helpful responses.

## Features ✨

- 💬 Interactive chatbot interface
- 🧠 NLP-based question understanding
- 📚 FAQ knowledge base integration
- 🔍 TF-IDF based text vectorization
- 📊 Cosine Similarity for question matching
- 🔄 Conversation memory with recent chat history
- 💡 Related question suggestions
- ⚠️ Fallback response for unknown questions
- 🌐 Flask-based web application

## Technologies Used 🛠️

- Python
- Flask
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Cosine Similarity
- HTML/CSS
- JSON

## How It Works ⚙️

1. FAQ data is loaded from a JSON file.
2. Questions from the FAQ dataset are converted into TF-IDF vectors.
3. User questions are converted into vector form.
4. Cosine Similarity compares the user query with stored questions.
5. The chatbot returns the most relevant answer.
6. If no suitable answer is found, a fallback response is provided.
7. Recent conversations are stored using session-based memory.

## Project Structure 📂

StudyBuddy_AI/
│
├── app.py              # Main Flask application
├── faq_data.json       # FAQ knowledge base
├── requirements.txt    # Required libraries
├── README.md           # Project documentation
└── .gitignore          # Ignored files


## Installation & Setup 🚀

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_LINK

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The chatbot will run on:

http://127.0.0.1:5000


## Example 💡

User:
How can I improve my concentration while studying?

StudyBuddy AI:
Provides a relevant study answer based on the FAQ knowledge base.


## Future Improvements 🚀

- Integration with Large Language Models
- Voice-based interaction
- Larger FAQ dataset
- Cloud deployment
- Improved personalization


## Author

Niharika Pyneni