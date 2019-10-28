import requests
from bs4 import BeautifulSoup
import os
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
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #print(title)
        url_second = "https://food.ltn.com.tw/" + title_first.a["href"]
        #print(insideurl)
        res_second = requests.get(url_second, headers=headers)
        soup_second = BeautifulSoup(res_second.text, 'html.parser')
        soup_second.select()
    except TypeError as e:
        print(e)



