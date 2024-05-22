import requests
import json
import os

# Read the webhook URL from an environment variable
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

# Ensure the webhook URL is set correctly
if not webhook_url:
    raise ValueError("WEBHOOK_URL is not set")

# Example message
meddelande = "Johannes>theo!"

# Send the message to the Discord webhook
skicka_discord_meddelande(webhook_url, meddelande)
