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


def write_line_into_csv_shopline():

    return 0


def main():
# Define Constant
    pattern = r'^(.+)/(W|S)(E?)([0-9]+)-([0-9+])$'

    print("歡迎使用WS 官網卡片爬蟲")
    print("POS .csv 模板：ShopLine")
    print("資料來源：https://ws-tcg.com/")
    print("請輸入目標彈數第一張卡")

    set_no = ""
    while(True):
    # 加入Regex 檢查輸入是否正確
        set_no = input("例子：PJS/S109-113")
        if re.match(pattern, set_no):
            break
        else:
            # 睇下之後有冇時間加function 去解䆁點解not match.
            print("輸入不符合要求，請重新輸入。")
    # Maybe need a sample output for first card.
    # As there have no way for me to check whether


    return 0


main()
