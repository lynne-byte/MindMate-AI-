CRISIS_KEYWORDS = [
    'suicide', 'suicidal', 'kill myself', 'end my life', 'want to die',
    'no reason to live', 'better off dead', 'harm myself', 'self harm',
    'cutting myself', 'overdose', 'jump off', 'hang myself'
]

HELPLINE_MESSAGE = 'I am concerned about you and I care about your safety. Please reach out for help immediately: Befrienders Kenya: 0800 723 253 (free, 24/7). Mathare Hospital Emergency: 0800 120 320. Chiromo Hospital: 0711 048 000. You are not alone. Help is available right now.'

def check_crisis(user_input):
    text = user_input.lower()
    for keyword in CRISIS_KEYWORDS:
        if keyword in text:
            return True
    return False

def get_crisis_response():
    return HELPLINE_MESSAGE
