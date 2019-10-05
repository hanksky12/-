import requests
from bs4 import BeautifulSoup
import os
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
path=r'./homework1.2'  #資料夾
if not os.path.exists(path): #沒有這個資料夾就新創資料夾
    os.mkdir(path)
page_number=3998

while page_number>=3988 :
    urlll=r"https://www.ptt.cc/bbs/sex/index%s.html"%(page_number)
    ss=requests.session()
    ss.cookies["over18"]="1"
    res=ss.get(urlll,headers=headerss)
    soup=BeautifulSoup(res.text,"html.parser")
    every_title =soup.select("div[class='title']")
    for n,title_name in enumerate(every_title):
        try:
            inside_url="https://www.ptt.cc"+title_name.a["href"]
            inside_res = ss.get(inside_url, headers=headerss)
            inside_soup = BeautifulSoup(inside_res.text, "html.parser")
            inside_title=inside_soup.select("div[id='main-content']")
            inside_paper=""#用一個變數接住所有要寫入的內容
            push_up = 0
            push_down = 0
            t1 = inside_soup.select('span[class="hl push-tag"]')
            t2 = inside_soup.select('span[class="f1 hl push-tag"]')
            t3 = inside_soup.select('div[class="article-metaline"]')
            for k in t1:#計算推數
                if "推" in k.text:
                    push_up += 1
            for p in t2:#計算噓數
                if "噓" in p.text:
                    push_down += 1

            inside_paper=inside_title[0].text.split("--")[0].split("2019")[1]   #寫入文章本文
            inside_paper += "~~~~~~~~~~split~~~~~~~~~~~~~" + "\n"
            inside_paper += "推:" + str(push_up) + "\n"   #寫入文章推
            inside_paper += "噓:" + str(push_down) + "\n" #寫入文章噓
            inside_paper += "得分:" + str(push_up - push_down) + "\n" #寫入文章分數
            inside_paper += t3[0].text + "\n" + t3[2].text +"\n"+t3[1].text+"\n"  #寫入作者=t3[0] 標題=t3[2] 時間=t3[1]
            try:
                with open("%s/%s.txt"%(path,title_name.a.text.replace('/', '-')),"w",encoding="utf-8") as f:
                    f.write(inside_paper.lstrip())

            except OSError:
                with open("%s/artic%s.txt"%(path, n),"w",encoding="utf-8") as f2:
                    f2.write(inside_paper.lstrip())
        # except AttributeError:#抓住已刪除的文章 不要讓它變成系統錯誤
        #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #     print("e.args")
        #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # except TypeError:#抓住刪除文章的另一種錯誤 不要讓它變成系統錯誤
        #     print("######################")
        #     print("TypeError")
        #     print("######################")
        except IndexError:#抓住刪除文章的另一種錯誤 不要讓它變成系統錯誤
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("IndexError")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    page_number -= 1