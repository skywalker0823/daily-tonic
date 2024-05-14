import datetime
import dotenv
import requests
import os
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 获取 Telegram 配置
def get_telegram_config():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN"),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID")
    }

# 发送消息到 Telegram
def send_telegram_message(text, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    return response.json()

# 测试函数
def tester():
    logger.info("---{}---".format(datetime.datetime.now()))
    config = get_telegram_config()
    logger.info("Telegram Config: {}".format(config))
    response = send_telegram_message("Test message from function-daily-tonic", config["TELEGRAM_TOKEN"], config["TELEGRAM_CHAT_ID"])
    logger.info("Telegram Response: {}".format(response))

if __name__ == "__main__":
    tester()
