import base64
import datetime
import dotenv
import os
import requests

import functions_framework


# from fastapi import FastAPI


def get_telegram_config():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN_V1", os.getenv("TELEGRAM_TOKEN")),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID_V1", os.getenv("TELEGRAM_CHAT_ID"))
    }


def send_telegram_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    return response.json()


def get_nasa():
    print("fetching nasa APOD...")


@functions_framework.cloud_event
def start_daily(cloud_event):
    print("---" + str(datetime.datetime.now()) + "---")
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    config = get_telegram_config()
    messages = [
        {"text": "Message from function-daily-tonic at" + str(datetime.datetime.now())},
        {"text": "https://digital-transformation.media/wp-content/uploads/2018/09/logo_gcp_vertical_rgb.png" + str(
            datetime.datetime.now())},
    ]
    for message in messages:
        response = send_telegram_message(message["text"], config["TELEGRAM_TOKEN"], config["TELEGRAM_CHAT_ID"])
        print(response)
