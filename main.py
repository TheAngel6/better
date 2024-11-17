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
meddelande = "https://x.com/DonaldJTrumpJr/status/1858136498530374074?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1858136498530374074%7Ctwgr%5Ebeaef782ccb60b0c0ce8dc7478eb7d5941abf412%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Fwww.foxnews.com%2Fpolitics%2Ftrump-inner-circle-shares-mcdonalds-meal-donald-jr-jokes-make-america-healthy-again-starts-tomorrow"

# Call the function to send the message
skicka_discord_meddelande(webhook_url, meddelande)
