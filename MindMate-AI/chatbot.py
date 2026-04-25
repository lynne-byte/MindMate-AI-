import json
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab", quiet=True)

with open ("responses/english.json",  "r") as f:
    responses=json.load(f)

def match_intent(user_input):
        tokens=word_tokenize(user_input.lower())
        for intent, data in responses.items():
            if intent =="unknown":
                continue
            for keyword in data ["keywords"]:
                if keyword in tokens or keyword in user_input.lower():
                    return intent
        return "unknown"
def get_response(intent):
    return random.choice(responses[intent]["responses"])

def chat (user_input):
    intent =match_intent(user_input)
    response =get_response(intent)
    return response
