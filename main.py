import requests
import json
import os

# Define the raw URL of the .webp image from GitHub
image_url = "https://raw.githubusercontent.com/TheAngel6/better/main/image%20(3).webp"

webhook_url = os.getenv('WEBHOOK_URL')

def skicka_discord_meddelande(webhook_url, meddelande, image_url):
    data = {
        "content": meddelande,
        "embeds": [
            {
                "image": {
                    "url": image_url
                }
            }
        ]
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

meddelande = "..."

skicka_discord_meddelande(webhook_url, meddelande, image_url)
