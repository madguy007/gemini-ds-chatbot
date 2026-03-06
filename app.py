import gradio as gr
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_gemini(user_input):

    prompt = f"""
    You are a Senior Data Scientist at Google specializing in machine learning and data analysis.
    Explain concepts clearly.

    User: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def chatbot_interface(user_input):
    return chat_with_gemini(user_input)


iface = gr.Interface(
    fn=chatbot_interface,
    inputs="text",
    outputs="text",
    title="Gemini Chatbot",
    description="Chatbot powered by Gemini 2.5 Flash. Ask me anything!"
)

iface.launch()