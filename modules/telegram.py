import requests
from . import module_configs

def send_telegram_message(text):
    module_config = module_configs()
    url = f"https://api.telegram.org/bot{module_config["TELEGRAM_TOKEN"]}/sendMessage"
    params = {"chat_id": module_config["TELEGRAM_CHAT_ID"], "text": text}
    response = requests.get(url, params=params)
    return response.json()
