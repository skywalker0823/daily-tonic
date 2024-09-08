import base64
import datetime
import functions_framework

# 擷取列
from fetch_list.bt import get_bt
from fetch_list.nasa import get_nasa

# 模組列
from modules.telegram import send_telegram_message
from modules.ptt_beauty import get_ptt_beauty


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
        response = send_telegram_message(text = message["text"], image_sets=None)
        print(response)

    result = send_telegram_message(None, get_ptt_beauty())
    print(result)

# if __name__ == "__main__":
#     start_daily()