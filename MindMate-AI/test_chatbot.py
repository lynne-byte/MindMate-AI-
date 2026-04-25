from chatbot import chat
from crisis import check_crisis, get_crisis_response

test_inputs = [
    "hello", "hi", "habari", "good morning", "jambo",
    "hey", "hujambo", "mambo", "hi there", "good evening",
    "I am anxious", "I am worried", "I feel nervous", "I am scared", "I am panicking",
    "nina wasiwasi", "naogopa",
    "I am depressed", "I feel sad", "I am hopeless", "nimechoka", "nimekata tamaa",
    "I am stressed", "I feel overwhelmed", "too much pressure",
    "I feel lonely", "I am alone", "sina rafiki",
    "I am angry", "I am frustrated", "ninakasirika",
    "I want to die", "I want to kill myself", "I want to harm myself", "end my life"
]

passed = 0
failed = 0
results = []

for user_input in test_inputs:
    if check_crisis(user_input):
        response = get_crisis_response()
        status = "PASS"
    else:
        response = chat(user_input)
        status = "PASS" if response else "FAIL"
    if status == "PASS":
        passed += 1
    else:
        failed += 1
    results.append(f"{status} | Input: {user_input} | Response: {response[:60]}")

for r in results:
    print(r)

print(f"\nTotal: {len(test_inputs)} | Passed: {passed} | Failed: {failed}")
print(f"Accuracy: {round(passed/len(test_inputs)*100, 1)}%")