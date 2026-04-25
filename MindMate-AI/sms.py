import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = "sandbox"
api_key = os.getenv("AT_API_KEY")

africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number], sender_id="MindMate")
        print("SMS sent: " + str(response))
        return True
    except Exception as e:
        print("SMS error: " + str(e))
        return False
if __name__ == "__main__":
    send_sms("+254712626755", "Hello from MindMate AI!")