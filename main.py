import base64
import datetime
import dotenv
import os
import requests

import functions_framework


# from fastapi import FastAPI


def get_configs():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN_V1", os.getenv("TELEGRAM_TOKEN")),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID_V1", os.getenv("TELEGRAM_CHAT_ID")),
        "NASA_KEY": os.getenv("NASA_KEY_V1", os.getenv("NASA_KEY"))
    }


def send_telegram_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    return response.json()


def get_nasa(config):
    print("fetching nasa APOD...")
    nasa_url = f'https://api.nasa.gov/planetary/apod?api_key={config["NASA_KEY"]}'
    try:
        nasa_response = requests.get(nasa_url)
        if nasa_response.status_code == 200:
            nasa_data = nasa_response.json()
            nasa_image = nasa_data["url"]
            nasa_explanation = nasa_data["explanation"]
            return {"nasa_image": nasa_image, "nasa_explanation": nasa_explanation}
    except:
        print("Fetching failed! There is something wrong with request to the NASA API.")
        return {"nasa_image": "image fetching failed", "nasa_explanation": "explanation fetching failed"}
    


@functions_framework.cloud_event
def start_daily(cloud_event):
    print("---" + str(datetime.datetime.now()) + "---")
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    config = get_configs()
    nasa_apod = get_nasa(config)
    messages = [
        {"text": "Message from function-daily-tonic at" + str(datetime.datetime.now())},
        {"text": nasa_apod["nasa_image"]},
        {"text": nasa_apod["nasa_explanation"]}
    ]
    for message in messages:
        response = send_telegram_message(message["text"], config["TELEGRAM_TOKEN"], config["TELEGRAM_CHAT_ID"])
        print(response)
