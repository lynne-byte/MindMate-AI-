import socket
from chatbot import chat
from crisis import check_crisis, get_crisis_response
from gemini import gemini_chat

def is_online():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def mood_checkin():
    print("MindMate: How would you rate your mood right now?")
    print("  1 - Very bad")
    print("  2 - Bad")
    print("  3 - Okay")
    print("  4 - Good")
    print("  5 - Very good")
    rating = input("You (1-5): ")
    if rating == "1":
        print("MindMate: I am sorry to hear that. I am here for you. Tell me what is going on.\n")
    elif rating == "2":
        print("MindMate: That sounds tough. Would you like to talk about it?\n")
    elif rating == "3":
        print("MindMate: Okay is a good place to start. How can I support you today?\n")
    elif rating == "4":
        print("MindMate: Glad to hear that! What has been going well?\n")
    elif rating == "5":
        print("MindMate: That is wonderful! Keep doing what is working for you.\n")
    else:
        print("MindMate: Thank you for sharing. How can I help you today?\n")

print("MindMate AI - Mental Health Chatbot")
print("Type 'quit' to exit | Type 'mood' for a mood check-in")
print()

if is_online():
    print("Mode: Online (Gemini AI)")
else:
    print("Mode: Offline (Basic responses)")
print()

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("MindMate: Take care. Remember, help is always available.")
        break
    elif user_input.lower() == "mood":
        mood_checkin()
    elif check_crisis(user_input):
        print("MindMate: " + get_crisis_response())
    elif is_online():
        response = gemini_chat(user_input)
        if response:
            print("MindMate: " + response)
        else:
            print("MindMate: " + chat(user_input))
    else:
        print("MindMate: " + chat(user_input))
    print()