import logging
import os

import dotenv
import requests

# 配置logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Get Telegram 配置
def get_configs():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN_V1", os.getenv("TELEGRAM_TOKEN")),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID_V1", os.getenv("TELEGRAM_CHAT_ID")),
        "NASA_KEY": os.getenv("NASA_KEY_V1", os.getenv("NASA_KEY"))
    }


# Send to Telegram
# def send_telegram_message(text, token, chat_id):
#     url = f"https://api.telegram.org/bot{token}/sendMessage"
#     params = {"chat_id": chat_id, "text": text}
#     response = requests.get(url, params=params)
#     return response.json()

# # 測試 def tester(): logger.info("---{}---".format(datetime.datetime.now())) config = get_configs() logger.info(
# "Telegram Config: {}".format(config)) response = send_telegram_message("Test message from function-daily-tonic",
# config["TELEGRAM_TOKEN"], config["TELEGRAM_CHAT_ID"]) logger.info("Telegram Response: {}".format(response))

def get_nasa():
    config = get_configs()
    nasa_url = f'https://api.nasa.gov/planetary/apod?api_key={config["NASA_KEY"]}'
    nasa_response = requests.get(nasa_url)
    if nasa_response.status_code == 200:
        nasa_data = nasa_response.json()
        nasa_image = nasa_data["url"]
        nasa_explanation = nasa_data["explanation"]
        print(nasa_image, nasa_explanation)


if __name__ == "__main__":
    # tester()
    get_nasa()
