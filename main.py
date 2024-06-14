import requests
import json
import os

webhook_url = os.getenv('WEBHOOK_URL')

def skicka_discord_meddelande(webhook_url, meddelande):
    data = {
        "content": meddelande
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Meddelandet har skickats till Discord!")
    else:
        print(f"Det uppstod ett fel: {response.status_code}, {response.text}")

if not webhook_url:
    raise ValueError("WEBHOOK_URL is not set")

meddelande = "Johannes>theo, mexo blev hackad, han under mig har skill issue och jag har tagit studenten :partying_face:! Grattis alla andra som också tagit studenten 2024 och lycka till med framtiden! https://tenor.com/ncABPViuNYN.gif"

skicka_discord_meddelande(webhook_url, meddelande)
