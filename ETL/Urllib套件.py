#套件urllib的 練習
from urllib import request
from bs4 import BeautifulSoup
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}#header 裡面都是字典形式
urlll="https://www.ptt.cc/bbs/index.html"#要連的網址
reqqq=request.Request(url=urlll,headers=headerss)
res=request.urlopen(reqqq)
#403表示有反應 但是回傳錯誤
# #未寫read只回傳記憶體位址
# #b開頭表示後面是2進位編碼 所以要decode
#print(res.read().decode("utf-8"))
#用BS4裡的find findall

soup=BeautifulSoup(res.read().decode("utf-8"),"html.parser")#放入原始碼,用html轉換器
#print(soup)      #這裡的TYPE已經轉換為BeautifulSoup
s=soup.findAll("a",{"id":"logo"})  #findall(標籤 ,屬性<===字典格式)
#print(s[0])                        # 有[] 是個list
#print(s[0].TEXT)                  #TEXT  string抓文字
#print("")
s2=soup.findAll("div",{"id":"topbar"})
print(s2[0])
print(s2[0].a)                     # 取div裡面的標籤  a
print(s2[0].a["href"])             #a 的[屬性]
s3=soup.findAll("div",class_="board-title")#如果用 字典型態 不用底線
for i in s3:
    print(i.text)
print("")
#找標題 以及連結
s3=soup.findAll("div",class_="b-ent")
#print(s3)
len(s3)
#print(len(s3))
for j in range(len(s3)):
    a=soup.findAll("div",class_="board-name")
    print(a[j].text)
    print("https://www.ptt.cc"+s3[j].a["href"])
    print("")
