---
title: Gemini Data Science Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# Gemini Data Science Chatbot

An AI-powered chatbot that answers questions about **Data Science, Machine Learning, Python, SQL, and Statistics** using the Gemini large language model.

The chatbot provides concise explanations, coding examples, and conceptual understanding of data science topics through an interactive chat interface.

---

## Live Demo

Try the chatbot here:

[(https://huggingface.co/spaces/Mad-an/gemini-data-science-chatbot)](https://huggingface.co/spaces/Mad-an/gemini-data-science-chatbot)

---

## Features

- ChatGPT-style chat interface
- Answers machine learning and data science questions
- Generates Python examples for ML concepts
- Provides concise explanations (6–7 lines)
- Interactive web interface using Gradio
- Deployed online using Hugging Face Spaces

---

## Tech Stack

- Python
- Gemini API
- Gradio
- Hugging Face Spaces

---

## Project Structure

```
.
├── app.py
├── simple_chat.py
├── gemini_model_check.py
├── requirements.txt
└── README.md
```

### File Description

**app.py**  
Main web chatbot interface built with Gradio.

**simple_chat.py**  
Command-line chatbot version.

**gemini_model_check.py**  
Script to check available Gemini models.

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

Set your Gemini API key

```bash
export GEMINI_API_KEY=your_api_key_here
```

Run the application

```bash
python app.py
```

Open in browser

```
http://127.0.0.1:7860
```

---

## Example Questions

You can ask questions such as:

- What is overfitting in machine learning?
- Explain gradient descent
- Write Python code for logistic regression
- Difference between bagging and boosting
- What is cross validation?

---

## Deployment

This project is deployed using **Hugging Face Spaces**.

Hugging Face automatically installs dependencies from `requirements.txt` and runs the Gradio application.

---

## Author

Madan Dahiphale

LinkedIn  
https://www.linkedin.com/in/madandahiphale
