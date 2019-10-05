import requests
from bs4 import BeautifulSoup
import os
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
path=r'./res'

if not os.path.exists(path):
    os.mkdir(path)
page_number=8316
while page_number>=8310 :
    urlll=r"https://www.ptt.cc/bbs/movie/index%s.html"%(page_number)
    res=requests.get(urlll,headers=headerss)
    soup=BeautifulSoup(res.text,"html.parser")
    title3 =soup.select("div[class='title']")
    for n,i in enumerate(title3):
        try:
            #print(i.a.text) #i.text 有上下空行
            insideurl="https://www.ptt.cc"+i.a["href"]     #請複習20190914
            #print(insideurl)
            #準備再進入每個連結內的文章 作法同之前
            insideres = requests.get(url=insideurl, headers=headerss)
            insidesoup = BeautifulSoup(insideres.text, "html.parser")
            insidetitle=insidesoup.select("div[id='main-container']")

            insidepaper=insidetitle[0].text.split("--")[0]
            #print(insidepaper)  #.split將STR分成list出來 前段是文章 後段是推文
            print(i.a.text)
            try:
                with open("%s/%s.txt"%(path,i.a.text.replace('/', '-')),"w",encoding="utf-8") as f:
                    f.write(insidepaper)

            except OSError:
                with open("%s/artic%s.txt"%(path, n),"w",encoding="utf-8") as f2:
                    f2.write(insidepaper)
            push_up = 0
            push_down = 0
            t1 = insidesoup.select('span[class="hl push-tag"]')
            t2 = insidesoup.select('span[class="f1 hl push-tag"]')
            for k in t1:
                if "推" in k.text:
                    push_up += 1
            for p in t2:
                if "噓" in p.text:
                    push_down += 1
            a = "推:" + str(push_up) + "\n"
            b = "噓:" + str(push_down) + "\n"
            c = "~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
            d = "得分:" + str(push_up - push_down) + "\n"
            try:
                with open("%s/%s.txt" % (path, i.a.text.replace('/', '-')), "a",
                          encoding="utf-8") as f:  # 這邊的/  因為這裡是絕對路徑 前面是資料夾 後面是檔名
                    f.write("\n" + a + b + c + d)
            except OSError:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        except AttributeError:#抓住已刪除的文章 不要讓它變成系統錯誤
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("e.args")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        except TypeError:#抓住刪除文章的另一種錯誤 不要讓它變成系統錯誤
            print("######################")
            print("TypeError")
            print("######################")
    page_number -= 1