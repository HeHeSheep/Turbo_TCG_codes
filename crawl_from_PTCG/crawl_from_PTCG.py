#PTCG 官網卡片爬蟲
#This program is to crawl the data from PTCG TC website
#Data that we need: webpage_No, Handle, 卡名, 彈數, 編號, 種類, 對戰標記, 卡圖連結
#After crawling, we need to save the data into a csv file preassigned by Shopify
#為相同名字卡片共用一個Handle, 例如: 高級球 共同使用一個Handle， 並用Option1 Value 來區分不同的 彈數＋編號

import requests, bs4, re, csv


def remove_spaces_and_tag(blank_word):
    blank_word = blank_word.strip()
    blank_word = blank_word.strip("\n")
    return blank_word

def main():
    webpage_No_start = int(input("請輸入起始卡片網頁編號")) #輸入起始卡片網頁編號
    webpage_No_end = int(input("請輸入結尾卡片網頁編號")) #輸入結尾卡片網頁編號

    #Create a csv file
    #Before using this program, please change the path of the csv file at line 92
    csvFile = open("/Users/Yeung/Downloads/PTCG_data " + str(webpage_No_start) +" to " +str(webpage_No_end) + ".csv", 'w', newline = '', encoding= 'UTF-8') 
    csvWriter = csv.writer(csvFile)
    #initial the csv file as Shopify required
    #Values in class are located in .csv at:

    csvWriter.writerow(['Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item', 'Included / 中國香港特別行政區', 'Price / 中國香港特別行政區', 'Compare At Price / 中國香港特別行政區', 'Included / 國際', 'Price / 國際', 'Compare At Price / 國際', 'Status'])
    #上面這行是設定csv檔的第一行，也就是每一個欄位的名稱，這邊是參考Shopify的csv檔格式
    #initial complete, start crawling in for loop below.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for webpage_No_start in range(webpage_No_start, webpage_No_end + 1):
        url = "https://asia.pokemon-card.com/hk/card-search/detail/" + str(webpage_No_start) #url of the card
        htmlfile = requests.get(url) #get the html file from the url

        if htmlfile.status_code != 200: #check if the webpage is downloaded successfully
            csvWriter.writerow([webpage_No_start + "網頁下載失敗，狀態為:" + str(htmlfile.status_code)]) #記錄錯誤網頁編號
            continue #提早結束迴圈，繼續執行下一次迴圈
        
        objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml') #將html轉成BeautifulSoup物件
        if objSoup.find('title').text == "卡牌搜尋結果 | 訓練家網站":
            continue #提早結束迴圈，繼續執行下一次迴圈
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
          #種類: 招式 == 寶可夢卡/ 寶可夢道具/ 物品卡/ 支援者卡/ 競技場卡/ 基本能量卡/ 特殊能量卡
          種類 = objSoup.find('h3', class_ ="commonHeader").text
        except: 
            種類 = "Error"
        else:
            種類 = remove_spaces_and_tag(種類) #清除資料前後的空格和換行標記
            if 種類 == "基本能量卡": #討論是否不需要保存基本能量卡資料。結論：不需要
                continue #提早結束迴圈，繼續執行下一次迴圈
            elif 種類 == "招式": 
                種類 = "寶可夢卡"
            #種類完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        卡名 = objSoup.find('li', class_ ="current").text
        卡名 = remove_spaces_and_tag(卡名) #清除資料前後的空格和換行標記
        if 卡名 == "1":
            卡名 = 'Error'
        #卡名完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #skillInformation
        cardInformationColumn = ""
        #效果HTML提取，用作Body (HTML) by 洋
        #呢度唔做住，能用就行，留待後人繼續努力 by 洋， 11/1/2024
        # try:
        #     cardInformationColumn = objSoup.find('div', class_ ="cardInformationColumn") #Receiving a BeautifulSoup object
        #     # skillInformation_html = str(skillInformation.prettify())  # 轉換BeautifulSoup object為字符串並格式化
        # except:
        #     cardInformationColumn = "Error"
        #效果HTML提取完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        #討論係咪要卡圖？ (要)
        try:
            linkTag = objSoup.select("section.imageColumn img") #提取卡圖連結的 HTML Tag
        except:
            卡圖連結 = "Error"
        else: 
            for link in linkTag:
                卡圖連結 = link.get('src') #從 HTML Tag 提取卡圖連結
        #卡圖連結完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        #討論需不需要對戰標記？ (Hold up this part first, need some time to understand the old code)
        #要，用作産品標籤 by 洋
        try:
            對戰標記 = objSoup.find('span', class_ ="alpha").text
        except:
            對戰標記 = "Error"
        else:
            對戰標記 = remove_spaces_and_tag(對戰標記)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #下面係彈數＋編號
        #彈數
        try:
            linkTag = objSoup.select("section.expansionLinkColumn a") #提取擴充包角標連結的 HTML Tag
        except:
            彈數 = "Error"
        else: 
            for link in linkTag:
                彈數 = link.get('href') #從 HTML Tag 提取擴充包角標連結
                彈數 = re.sub(r'^.*?=', '', 彈數, 0) #利用正則表達式清除多餘部分

        #編號：用作支撐Handle 的唯一性。
        try:
            編號 = objSoup.find('span', class_ ="collectorNumber").text
        except:
            編號 = "Error"
        else:
            編號 = remove_spaces_and_tag(編號)
            編號 = re.sub(r'/.*?$', '', 編號, 0) #清除 / 後所有字, eg: '090/190' => '090'。 討論需不需要清除前置0？
            # 編號 = re.sub(r'^0', '', 編號, 0) #清除前置0
            編號 = re.sub(r'^0', '', 編號, 0) #清除前置0      
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #産品標籤（標籤）： 支持自動加入到篩選條件分組
        #産品標籤包含： 遊戲名稱（PTCG）、卡片種類(e.g.:寶可夢卡)、彈數(e.g.: SV4a)、對戰標記(e.g.:F)
        産品標籤 = "PTCG, " + 種類 + ", " + 彈數 + ", " + 對戰標記
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Handle 例子：高級球(sv4a)
        Handle = 卡名 + " (" + 彈數 + "_" + 編號 + ")"
        #Handle完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Error checking
        if 卡名 == 種類 == 對戰標記:
            continue
        #Error checking完成
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #將資料寫入csv檔
        #                 'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item', 'Included / 中國香港特別行政區', 'Price / 中國香港特別行政區', 'Compare At Price / 中國香港特別行政區', 'Included / 國際', 'Price / 國際', 'Compare At Price / 國際', 'Status'] 
        csvWriter.writerow([Handle, 卡名, cardInformationColumn, "Turbo TCG",                "",     "", 産品標籤, "FALSE",            "Title", "Default Title",             "",              "",             "",              "",            "",             "0",                   "shopify",                     "0",                     "deny",                      "manual",             "0",                         "",                      "TRUE",            "TRUE",                "",     卡圖連結,              "1",               "",     "FALSE", "", "", "", "", "", "", "", "", "", "", "", "", "", "",                                                                                                                                                                                                                                                                                                                                                                                                   "kg", "",                              "",                       "TRUE",                        "",                                   "", "TRUE",        "",            "","draft"])
        #將資料寫入csv檔完成
        #one loop ends
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
    csvFile.close()
    print("全部資料下載完畢。")
    #main() ends
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
main()