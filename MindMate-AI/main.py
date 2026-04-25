from chatbot import chat
from crisis import check_crisis, get_crisis_response

print("MindMate AI - Mental Health Chatbot")
print("Type 'quit' to exit")
print()

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("MindMate: Take care. Remember, help is always available.")
        break
    if check_crisis(user_input):
        print("MindMate: " + get_crisis_response())
    else:
        response = chat(user_input)
        print("MindMate: " + response)
    print()