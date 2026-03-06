import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_gemini(user_input):

    prompt = f"""
    You are a Senior Data Scientist at Google specializing in machine learning.
    Answer the user's question clearly.

    User: {user_input}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def run_chatbot():
    print("Welcome to Gemini Chatbot. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        response = chat_with_gemini(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    run_chatbot()