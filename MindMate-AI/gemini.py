import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = "You are MindMate, a mental health chatbot for Kenya. Provide CBT support in English or Swahili. Keep responses short and warm. If crisis, mention Befrienders Kenya: 0800 723 253."

def gemini_chat(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=SYSTEM_PROMPT + " User: " + user_input
        )
        return response.text
    except Exception as e:
        print("Gemini error: " + str(e))
        return None