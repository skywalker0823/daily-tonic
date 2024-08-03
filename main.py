import base64
import datetime
import functions_framework

# 擷取列
from fetch_list.bt import get_bt
from fetch_list.nasa import get_nasa

# 模組列
from modules.telegram import send_telegram_message


@functions_framework.cloud_event
def start_daily(cloud_event):
    print("---" + str(datetime.datetime.now()) + "---")
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    nasa_apod = get_nasa()
    messages = [
        {"text": "Message from function-daily-tonic at " + str(datetime.datetime.now())},
        {"text": nasa_apod["nasa_image"]},
        {"text": nasa_apod["nasa_explanation"]}
    ]
    for message in messages:
        response = send_telegram_message(text = message["text"])
        print(response)
