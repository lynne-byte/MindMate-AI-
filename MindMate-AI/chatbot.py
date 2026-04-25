import json
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab", quiet=True)

with open("responses/english.json", "r") as f:
    english_responses = json.load(f)

with open("responses/swahili.json", "r") as f:
    swahili_responses = json.load(f)

def detect_language(user_input):
    swahili_words = ["habari", "mambo", "salam", "hujambo", "jambo", "wasiwasi",
                     "hofu", "huzuni", "hasira", "peke", "niko", "nina", "sijisikii"]
    text = user_input.lower()
    for word in swahili_words:
        if word in text:
            return "swahili"
    return "english"

def match_intent(user_input, responses):
    text = user_input.lower()
    tokens = word_tokenize(text)
    for intent, data in responses.items():
        if intent == "unknown":
            continue
        for keyword in data["keywords"]:
            if keyword in tokens or keyword in text:
                return intent
    return "unknown"

def get_response(intent, responses):
    return random.choice(responses[intent]["responses"])

def chat(user_input):
    language = detect_language(user_input)
    if language == "swahili":
        intent = match_intent(user_input, swahili_responses)
        return get_response(intent, swahili_responses)
    else:
        intent = match_intent(user_input, english_responses)
        return get_response(intent, english_responses)