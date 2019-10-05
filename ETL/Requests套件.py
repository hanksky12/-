import requests
from bs4 import BeautifulSoup
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
urlll="https://www.ptt.cc/bbs/index.html"

res=requests.get(url=urlll,headers=headerss)# 前面不寫url= 也可
print(res)
soup=BeautifulSoup(res.text,"html.parser")
#print(soup)
title=soup.select("a.board") #與findall差不多 出來會是LIST
#print(title)
print("")
title2=soup.select("a[class='board']") #與上面寫法不同 結果一樣    如果裡面有兩個引號必加"a[class="board"]" 所以都加引號
#print(title2)
'''
for i in title:
    print(i.text)
'''
#電影標題 連結抓出來
urlll="https://www.ptt.cc/bbs/movie/index.html"
res=requests.get(url=urlll,headers=headerss)# 前面不寫url= 也可
print(res)
soup=BeautifulSoup(res.text,"html.parser")
title3 =soup.select("div[class=title]")
#print(title3)
for i in title3:
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
