import requests
from bs4 import BeautifulSoup
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
urlll="https://www.ptt.cc/bbs/movie/index.html"
for i in range(0,5):#0到5頁
    res=requests.get(urlll,headers=headerss)
    soup=BeautifulSoup(res.text,"html.parser")
    title3 =soup.select("div[class=title]")
    for i in title3:
        try:
            print(i.a.text) #i.text 有上下空行
            insideurl="https://www.ptt.cc"+i.a["href"]#請複習20190914
            print(insideurl)
            #準備再進入每個連結內的文章 作法同之前
            insideres = requests.get(url=insideurl, headers=headerss)
            insidesoup = BeautifulSoup(insideres.text, "html.parser")
            insidetitle=insidesoup.select("div[id=main-container]")
            insidepaper=insidetitle[0].text.split("--")[0] #.split將STR分成list出來 前段是文章 後段是推文
            print(insidepaper)
            print("")
        except AttributeError:#抓住已刪除的文章 不要讓它變成系統錯誤
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("e.args")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    url_last="https://www.ptt.cc"+soup.select("a[class='btn wide']")[1]["href"]
    url=url_last #把上一頁的link 重新指定到url  回到for迴圈第一行 就會換頁