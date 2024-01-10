#This program is to crawl the data from PTCG TC website
#Data that we need: webpage_No, Handle, 卡名, 彈數, 編號, 種類, 對戰標記, 卡圖連結
#After crawling, we need to save the data into a csv file preassigned by Shopify
#為相同名字卡片共用一個Handle, 例如: 高級球 共同使用一個Handle， 並用Option1 Value 來區分不同的 彈數＋編號

import requests, bs4, re, csv

def remove_spaces_and_tag(blank_word):
    blank_word = blank_word.strip()
    blank_word = blank_word.strip("\n")
    return blank_word

class Card:
    def __init__(self, webpage_No, Handle, 卡名, 彈數, 編號, 種類, 對戰標記, 卡圖連結):
        self.webpage_No = webpage_No
        self.Handle = Handle
        self.卡名 = 卡名
        self.彈數 = 彈數
        self.編號 = 編號
        self.種類 = 種類
        self.對戰標記 = 對戰標記
        self.卡圖連結 = 卡圖連結

    def __str__(self):
        return self.webpage_No + ',' + self.Handle + ',' + self.卡名 + ',' + self.彈數 + ',' + self.編號 + ',' + self.種類 + ',' + self.對戰標記 + ',' + self.卡圖連結

    def __repr__(self):
        return self.webpage_No + ',' + self.Handle + ',' + self.卡名 + ',' + self.彈數 + ',' + self.編號 + ',' + self.種類 + ',' + self.對戰標記 + ',' + self.卡圖連結

def main():
    webpage_No_start = int(input("請輸入起始卡片網頁編號")) #輸入起始卡片網頁編號
    webpage_No_end = int(input("請輸入結尾卡片網頁編號")) #輸入結尾卡片網頁編號

    #Create a csv file
    csvFile = open("PTCG_data " + str(webpage_No_start) +" to " +str(webpage_No_end) + ".csv", 'w', newline = '', encoding= 'UTF-8') 
    csvWriter = csv.writer(csvFile)
    #initial the csv file as Shopify required
    #Values in class are located in .csv at:
    # Handle = Handle 用途：商品名稱，多種同卡名卡片會共用同一個Handle e.g.高級球
    # 卡名 = Title 用途：商品名稱，一個Handle只有一個Title e.g.高級球
    # 彈數 = 
    # 編號 = 
    # 種類 = 
    # 對戰標記 = 
    # 卡圖連結 = 
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
        
        卡名 = objSoup.find('li', class_ ="current").text
        卡名 = remove_spaces_and_tag(卡名) #清除資料前後的空格和換行標記
        if 卡名 == "1":
            卡名 = 'Error'
        #卡名完成
        
        #討論係咪要卡圖？ (要)
        try:
            linkTag = objSoup.select("section.imageColumn img") #提取卡圖連結的 HTML Tag
        except:
            卡圖連結 = "Error"
        else: 
            for link in linkTag:
                卡圖連結 = link.get('src') #從 HTML Tag 提取卡圖連結
        #卡圖連結完成
        
        #討論需不需要對戰標記？ (Hold up this part first, need some time to understand the old code)
        
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

        #編號
        try:
            編號 = objSoup.find('span', class_ ="collectorNumber").text
        except:
            編號 = "Error"
        else:
            編號 = remove_spaces_and_tag(編號)
            編號 = re.sub(r'/.*?$', '', 編號, 0) #清除 / 後所有字, eg: '090/190' => '090'。 討論需不需要清除前置0？
            編號 = re.sub(r'^0', '', 編號, 0) #清除前置0
            編號 = re.sub(r'^0', '', 編號, 0) #清除前置0      

        #産品標籤（標籤）： 支持自動加入到篩選條件分組
        #産品標籤包含： 遊戲名稱（PTCG）、卡片種類、彈數、對戰標記


main()