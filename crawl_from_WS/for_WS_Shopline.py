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


def main():
    print("歡迎使用WS 官網卡片爬蟲")
    print("POS .csv 模板：ShopLine")
    print("資料來源：https://ws-tcg.com/")
    print("")

    return 0


main()
