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
    if response.status_code == 200:
        print("Meddelandet har skickats till Discord!")
    else:
        print(f"Det uppstod ett fel: {response.status_code}")
# Ersätt "din_webhook_url_här" med din faktiska webhook-URL

webhook_url = "WEBHOOK_URL"
meddelande = "Johannes>theo!"
skicka_discord_meddelande(webhook_url, meddelande)
