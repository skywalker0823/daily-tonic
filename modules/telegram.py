import requests
from . import module_configs
import time

MAX_IMAGES_PER_BATCH = 10

def send_telegram_message(text,image_sets):
    module_config = module_configs()
    token = module_config["TELEGRAM_TOKEN"]
    url_msg = f"https://api.telegram.org/bot{token}/sendMessage"
    url_image_set = f"https://api.telegram.org/bot{token}/sendMediaGroup"
    if image_sets == False or image_sets == None:
        print("no images")
        params = {"chat_id": module_config["TELEGRAM_CHAT_ID"], "text": text}
        response = requests.get(url_msg, params=params)
        return response.json()
    

        #先送出主題 在送出組圖 組間休息幾秒鐘

        # 圖片若超過10 分兩次以上處理 tg 不能接受一次10張以上
        # 將文字改成文字超連結 方便除錯與去網站看原圖文
    else:
        print("has images")
        # image set example {title:[image_urls],title2:[image_urls]}
        params = {"chat_id": module_config["TELEGRAM_CHAT_ID"]}
        print(image_sets)
        for set_name in image_sets:
            print(set_name)

            # 處理 Title
            params = {"chat_id": module_config["TELEGRAM_CHAT_ID"], "text": set_name}
            response1 = requests.get(url_msg, params=params)
            print(response1.json())
        
            # 處理圖片 list
            images = image_sets[set_name]
            media = []
            for img in images:
                if len(media) == 10:
                    print("滿10 擲出---", media, "---準備寄出")
                    payload = {
                        "chat_id": module_config["TELEGRAM_CHAT_ID"],
                        "media": media
                    }
                    response2 = requests.post(url_image_set, json=payload)
                    # try again if 400
                    if response2.status_code == 400:
                        print("response2 code 400 重新嘗試中...")
                        payload = {
                        "chat_id": module_config["TELEGRAM_CHAT_ID"],
                        "media": media
                        }
                        response2 = requests.post(url_image_set, json=payload)
                    print(response2)
                    media = []
                    time.sleep(3)
                media.append({"type": "photo", "media": img})
            print("未滿10 擲出---", media, "---準備寄出")
            payload = {
                        "chat_id": module_config["TELEGRAM_CHAT_ID"],
                        "media": media
                    }
            response3 = requests.post(url_image_set, json=payload)
            if response3.status_code == 400:
                print("response3 code 400 重來...")
                payload = {
                        "chat_id": module_config["TELEGRAM_CHAT_ID"],
                        "media": media
                        }
                response3 = requests.post(url_image_set, json=payload)
            print(response3)
            time.sleep(3)
        return {"status":"0"}
            # media = [{"type": "photo", "media": img} for img in images]
            # payload = {
            #         "chat_id": module_config["TELEGRAM_CHAT_ID"],
            #         "media": media
            #     }
            # response2 = requests.post(url_image_set, json=payload)
            # print(response2.json())
            # time.sleep(3)








            # media = [{"type": "photo", "media": img} for img in images]
            # payload = {
            #     "chat_id": module_config["TELEGRAM_CHAT_ID"],
            #     "media": media
            # }
            # response2 = requests.post(url_image_set, json=payload)
            # print(response1.json(), response2.json())
            # time.sleep(3)

