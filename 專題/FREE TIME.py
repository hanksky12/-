import requests
from bs4 import BeautifulSoup
import os
import time

user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
headers={"user-agent":user_agenttt,
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"cache-control": "no-cache",
"pragma": "no-cache",
"referer": "https://food.ltn.com.tw/article/9373",
"sec-fetch-mode": "nested-navigate",
"sec-fetch-site": "cross-site",
"upgrade-insecure-requests": "1"}

path=r'./food'  #資料夾
if not os.path.exists(path): #沒有這個資料夾就新創資料夾
    os.mkdir(path)

#第一層
url_first="https://food.ltn.com.tw/category"
res_first = requests.get(url_first, headers=headers)
#print(res)
soup_first = BeautifulSoup(res_first.text, 'html.parser')
#p跟/p包含我要的五穀雜糧、肉類..，因為五穀雜糧下面的細項不點選就會全部在五穀頁面裡面，到下層連結只要用
titles_first = soup_first.select('p')
for title_first in titles_first:
    try:
        print("~~~~~~~~~~~~~~~~~~2_level~~~~~~~~~~~~~~~~~~~~~")
        #第二層第1頁
        url_second_level= "https://food.ltn.com.tw/" + title_first.a["href"] + "/" + str(1)
        res_second = requests.get(url_second_level, headers=headers)
        soup_second = BeautifulSoup(res_second.text, 'html.parser')
        page_tail=soup_second.select('a[class="p_last"]')
        page_last_number = page_tail[0]['href'].split("/")[5]
        # 第二層第2頁~最後一頁
        page_number=1
        while page_number <= int(page_last_number):
            url_second_level_every_page = "https://food.ltn.com.tw/" + title_first.a["href"]+"/"+str(page_number)
            res_second_every_page = requests.get(url_second_level_every_page, headers=headers)
            soup_second_every_page = BeautifulSoup(res_second_every_page.text, 'html.parser')
            url_thrds = soup_second_every_page.select('div[data-desc="清單"] a')
            #print(url_thrds)
            print(str(page_number)+"page"+"~~~~~~~~~~~~~~~~~~~")

            for url_thrd in url_thrds:
                #print(url_thrd["href"])
                url_thir_level="https://food.ltn.com.tw/"+url_thrd["href"]
                print(url_thir_level)
            page_number += 1







    except TypeError as e:
        print(e)



