import requests
from bs4 import BeautifulSoup
import os
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
path=r'./homework1'  #資料夾
if not os.path.exists(path): #沒有這個資料夾就新創資料夾
    os.mkdir(path)
page_number=4006


while page_number>=3996 :
    urlll=r"https://www.ptt.cc/bbs/sex/index%s.html"%(page_number)
    res=requests.get(urlll,headers=headerss,cookies={"over18":"1"})
    soup=BeautifulSoup(res.text,"html.parser")
    title3 =soup.select("div[class='title']")
    #print(title3)
    for n,i in enumerate(title3):
        try:
            insideurl="https://www.ptt.cc"+i.a["href"]
            insideres = requests.get(url=insideurl, headers=headerss,cookies={"over18":"1"})#這邊COOKIE要記得  用方法二較好
            insidesoup = BeautifulSoup(insideres.text, "html.parser")
            insidetitle=insidesoup.select("div[id='main-content']")
            insidepaper=insidetitle[0].text.split("--")[0].split("2019")[1]
            #print(type(insidepaper))  #.split將STR分成list出來 前段是文章 後段是推文
            #文章內文
            try:
                with open("%s/%s.txt"%(path,i.a.text.replace('/', '-')),"w",encoding="utf-8") as f:#這邊的/  因為這裡是絕對路徑 前面是資料夾 後面是檔名
                    f.write(insidepaper.lstrip())

            except OSError:
                with open("%s/artic%s.txt"%(path, n),"w",encoding="utf-8") as f2:
                    f2.write(insidepaper.lstrip())
            #計算推噓數
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
                with open("%s/artic%s.txt"%(path, n), "a",
                          encoding="utf-8") as f:  # 這邊的/  因為這裡是絕對路徑 前面是資料夾 後面是檔名
                    f.write("\n" + a + b + c + d)
            #print(type(insidesoup))
            #抓出作者 與 時間  自己觀察網頁 print 作者=t3[0]  時間=t3[1]
            t3 = insidesoup.select('div[class="article-metaline"]')
            try:
                with open("%s/%s.txt" % (path, i.a.text.replace('/', '-')), "a",
                          encoding="utf-8") as f:  # 這邊的/  因為這裡是絕對路徑 前面是資料夾 後面是檔名
                    f.write("\n" + t3[0].text + "\n" + t3[2].text +"\n"+t3[1].text+"\n")
            except OSError:
                with open("%s/artic%s.txt" % (path, n), "a",
                          encoding="utf-8") as f:
                    f.write("\n" + t3[0].text + "\n" + t3[2].text +"\n"+t3[1].text+"\n")

        except AttributeError:#抓住已刪除的文章 不要讓它變成系統錯誤
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("e.args")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        except TypeError:#抓住刪除文章的另一種錯誤 不要讓它變成系統錯誤
            print("######################")
            print("TypeError")
            print("######################")
        except IndexError:#抓住刪除文章的另一種錯誤 不要讓它變成系統錯誤
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("IndexError")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    page_number -= 1