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

print("MindMate AI - Mental Health Chatbot")
print("Type 'quit' to exit")
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
    if check_crisis(user_input):
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