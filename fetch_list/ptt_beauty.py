import requests
from bs4 import BeautifulSoup
import re
import os, time , random

# URL
BASE_URL = "https://www.ptt.cc"
PTT_URL = "https://www.ptt.cc/bbs/Beauty/index.html"
# https://www.ptt.cc/bbs/Beauty/index3995.html
TEST_URL = "https://www.ptt.cc/bbs/Beauty/index3887.html"

# 修改預定:
# 1. 擲出連結即可 不需下載
# 2. 隨機找圖 頁數預定1800~3998(2024/0908 最新頁) 最新-1 或指定日期
# 3. 列出 title as a url
# 4. webhook功能

def get_ptt_beauty():
# 設置 session 並通過年齡驗證
    session = requests.Session()
    session.cookies.set('over18', '1')

    # User-Agent 模擬瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 目標圖片存儲文件夾(存到本機用)
    # save_dir = "ptt_beauty_images"
    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)

    # 發送請求並解析 HTML
    # response = session.get(PTT_URL, headers=headers)
    # soup = BeautifulSoup(response.text, 'html.parser')

    #找出目前最新頁面的上一頁(預計用來取得接近最新)
    # pagination_bar = soup.find('div', class_='btn-group btn-group-paging')
    # previous_page_link = pagination_bar.find('a', string='‹ 上頁')['href']
    # print(f"Processing page: {previous_page_link}")

    number = random.randint(1800,4006)
    # 測試用(改這裡就好!)
    response = session.get(f"https://www.ptt.cc/bbs/Beauty/index{number}.html", headers=headers)
    # response = session.get(BASE_URL+previous_page_link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有文章(預計刪除公告)
    articles = soup.find_all('div', class_='r-ent')
    image_set = {}

    # 遍歷每篇文章 測試先限制抓兩篇即可
    for article in articles:
        title_tag = article.find('a')
        if title_tag:
            title = title_tag.text
            link = "https://www.ptt.cc" + title_tag['href']

            print(f"Processing article: {title}")

            # 發送請求到文章頁面
            article_response = session.get(link, headers=headers)
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            # 提取所有圖片連結
            img_urls = article_soup.find_all('a', href=re.compile(r'(https?://.*\.(jpg|jpeg|png|gif))'))
            for img_url in img_urls:
                time.sleep(1)
                img_link = img_url['href']
                print(f"Found image: {img_link}")
                image_set.setdefault(title, []).append(img_link)
    print("All img fetch finished")
    print(image_set)
    return image_set

                # # 發送請求下載圖片
                # img_response = session.get(img_link, headers=headers)

                # # 確保請求成功再保存圖片
                # if img_response.status_code == 200:
                #     img_name = os.path.join(save_dir, img_link.split('/')[-1])
                #     with open(img_name, 'wb') as img_file:
                #         img_file.write(img_response.content)
                #     print(f"Image saved to {img_name}")
                # else:
                #     print(f"Failed to download image: {img_link} (Status code: {img_response.status_code})")





# if __name__ == "__main__":
#     send_telegram_message(None, get_ptt_beauty())

# if __name__ == "__main__":
#     get_ptt_beauty()
