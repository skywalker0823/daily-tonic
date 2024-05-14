import base64
import functions_framework
import os, dotenv, datetime, requests
from fastapi import FastAPI


def get_telegram_config():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN_V1"),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID_V1")
    }


def send_telegram_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    return response.json()


# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def start_daily(cloud_event):
    # Print out the data from Pub/Sub, to prove that it worked
    print("---" + str(datetime.datetime.now()) + "---")
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    config = get_telegram_config()
    response = send_telegram_message("Test message from function-daily-tonic at" + str(datetime.datetime.now()),
                                     config["TELEGRAM_TOKEN"], config["TELEGRAM_CHAT_ID"])
    print(response)
