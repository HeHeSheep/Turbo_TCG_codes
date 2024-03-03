# WS 官網卡片爬蟲
# This program is to crawl card data from WS JP website
# Then assign into .csv file.


# Data specification:
# Target User: TopDraw.
# Target .csv template: ShopLine.
# Data that we need: Wait for TopDraw assign.


# Improve direction:
# 1. Def a function to save all information fetched from HTML in an array
# 2. Pass the array to another function and write line to .csv // Then start new loop
# Such that The part of fetching card info can be reused and suitable for different POS .csv template.


# Creator: Chin Tsz Yeung
# Email: oscarcty@gmail.com
# Discord: hehesheep
# ---------------------------------------------------------------------------------------------------------

import os.path
import requests
import bs4
import re
import csv
import re
class card_info:
    def __init__(self, card_name, card_no, neo_standard_define,
                 title_no, rare, side, card_type,
                 color, level, cost, power, soul, trigger,
                 attribute, text, favour_text, card_image_url, next_card_url):
        self.card_name = card_name
        self.card_no = card_no
        self.neo_standard_define = neo_standard_define
        self.title_no = title_no
        self.rare = rare
        self.side = side
        self.card_type = card_type
        self.color = color
        self.level = level
        self.cost = cost
        self.power = power
        self.soul = soul
        self.trigger = trigger
        self.attribute = attribute
        self.text = text
        self.favour_text = favour_text
        self.card_image_url = card_image_url
        self.next_card_url = next_card_url

def write_line_into_csv_shopline():
    return 0


def fetch_html(url):
    html_file = requests.get(url)  # fetch the html file from the url
    if html_file.status_code != 200:  # check if the webpage is downloaded successfully
        print(f'網頁拿取失敗，狀態為:{html_file.status_code}')# 輸出error code
        return 0
    objSoup = bs4.BeautifulSoup(html_file.text, 'html.parser')  # 將html轉成BeautifulSoup物件
    # Here may need sth to check if I am going to correct webpage

    return objSoup


def main():
    # Define Constant
    pattern = r'^(.+)/(W|S)(E?)([0-9]+)-([0-9+])$'

    print("歡迎使用WS 官網卡片爬蟲")
    print("POS .csv 模板：ShopLine")
    print("資料來源：https://ws-tcg.com/")
    print("請輸入目標彈數第一張卡")

    set_no = ""
    while True:
        # 加入Regex 檢查輸入是否正確
        set_no = input("例子：PJS/S109-113")
        if re.match(pattern, set_no):
            # Check if this input goes to where unexpected:
            url = f'https://ws-tcg.com/cardlist/?cardno={set_no}'
            soup = fetch_html(url)

            break
        else:
            # 睇下之後有冇時間加function 去解䆁點解not match.
            print("輸入不符合要求，請重新輸入。")
    # Maybe need a sample output for first card.
    # As there have no way for me to check whether

    return 0


main()
