import requests
from config import MAX_TOKEN, CHANNEL_ID

BASE_URL = "https://botapi.max.ru"


def send_message(text):
    url = f"{BASE_URL}/messages"

    headers = {
        "Authorization": f"Bearer {MAX_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)
