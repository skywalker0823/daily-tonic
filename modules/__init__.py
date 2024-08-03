import dotenv
import os

def module_configs():
    dotenv.load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN_V1", os.getenv("TELEGRAM_TOKEN")),
        "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID_V1", os.getenv("TELEGRAM_CHAT_ID"))
    }