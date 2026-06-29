# StudyBuddy AI 📚🤖

StudyBuddy AI is an AI-powered study assistant that helps users interact with their study materials. Users can upload documents and ask questions, and the application retrieves relevant information to provide helpful answers.

This project uses Natural Language Processing (NLP), sentence embeddings, and similarity-based retrieval techniques to understand user queries and provide relevant responses.

## Features ✨

- 📄 Upload and process study documents
- 💬 Interactive chat-style interface
- 🧠 Semantic search using sentence embeddings
- 🔍 Retrieves relevant information from uploaded content
- 🤖 AI-powered question answering
- ⚡ Fast similarity matching using cosine similarity
- 📚 Helps students understand study materials easily

## Technologies Used 🛠️

- Python
- Streamlit
- Sentence Transformers
- Transformers
- Scikit-learn
- NLP
- Cosine Similarity
- Tiktoken

## How It Works ⚙️

1. User uploads a document or study material.
2. Text is extracted and processed.
3. The extracted content is converted into embeddings.
4. User questions are converted into embeddings.
5. Cosine similarity is used to find the most relevant information.
6. The chatbot provides answers based on the retrieved context.

## Project Structure 📂

    StudyBuddy_AI/
    │
    ├── app.py
    ├── file_utils.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore


## Installation & Setup 🚀

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_LINK

Install dependencies:

    pip install -r requirements.txt

Run the application:

    streamlit run app.py


## Future Improvements 🚀

- Add long-term conversation memory
- Support more document formats
- Improve answer generation
- Deploy the application online


## Author

Niharika Pyneni
