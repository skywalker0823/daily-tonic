from fetch_list.bt import get_bt
from fetch_list.nasa import get_nasa

from modules.telegram import send_telegram_message



def tester():
    # nasa_result = get_nasa()
    # tg_result = send_telegram_message("hi hi world!")
    # print(nasa_result)
    # print(tg_result)
    print("test")

if __name__ == "__main__":
#    configs = get_configs()
#    send_telegram_message(text = "test message", token = configs["TELEGRAM_TOKEN"], chat_id = configs["TELEGRAM_CHAT_ID"])
    tester()