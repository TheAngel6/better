import requests
import json
import os

# Retrieve the webhook URL from environment variables
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

# Ensure that the webhook URL is provided
if not webhook_url:
    raise ValueError("WEBHOOK_URL is not set")

# Define the message you want to send
meddelande = "Dark Soldier är en gambler"

# Call the function to send the message
skicka_discord_meddelande(webhook_url, meddelande)
