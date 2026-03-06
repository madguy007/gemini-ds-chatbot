# Gemini Data Science Chatbot

A Data Science chatbot powered by the Google Gemini model that answers questions related to machine learning, statistics, Python, and data analysis.

This project demonstrates how to integrate a Large Language Model with a web interface to build an interactive AI assistant for learning and solving data science problems.

---

## Features

- Answer machine learning and data science questions
- Generate Python code examples
- Explain statistics and ML concepts
- Interactive web chatbot interface
- Command line chatbot version
- Model availability checker

---

## Tech Stack

- Python
- Google Gemini API
- Gradio (for web interface)
- python-dotenv

---

## Project Structure

```
gemini-data-science-chatbot/
│
├── app.py
├── simple_chat.py
├── gemini_model_check.py
├── requirements.txt
├── .env
└── README.md
```

**app.py**  
Gradio-based web chatbot interface.

**simple_chat.py**  
Command line chatbot version.

**gemini_model_check.py**  
Script used to check which Gemini models are available for the API key.

**requirements.txt**  
Project dependencies.

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-data-science-chatbot.git
cd gemini-data-science-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the project folder

```
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Web Chatbot

Run the Gradio application

```bash
python app.py
```

Then open your browser and go to

```
http://127.0.0.1:7860
```

---

## Run the Command Line Chatbot

```bash
python simple_chat.py
```

---

## Check Available Gemini Models

```bash
python gemini_model_check.py
```

This script lists the models available for your API key.

---

## Example Questions

You can ask questions such as:

- What is overfitting in machine learning?
- Explain gradient descent
- Write Python code for logistic regression
- Difference between bagging and boosting
- Explain bias vs variance

---

## Future Improvements

- Add conversation memory
- Add dataset upload and analysis
- Implement Retrieval Augmented Generation (RAG)
- Deploy the chatbot online
- Add streaming responses

---

## Author

Madan Dahiphale

LinkedIn  
https://www.linkedin.com/in/madandahiphale