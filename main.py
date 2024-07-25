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

meddelande = "skill issue! https://tenor.com/ncABPViuNYN.gif"

skicka_discord_meddelande(webhook_url, meddelande)
