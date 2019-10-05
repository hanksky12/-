import requests  #這邊教request的cookie     urllib簡單
from bs4 import BeautifulSoup
user_agenttt="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headerss={"user-agent":user_agenttt}
url="https://www.ptt.cc/bbs/Gossiping/index.html"
#cookie 方法一
res=requests.get(url=url,headers=headerss,cookies={"over18":"1"})#urllib 類似方法ㄧ
"""
#cookie 方法二
ss=requests.session()
ss.cookies["over18"]="1"  #1是str
res=ss.get(url,headers=headerss)
"""
soup=BeautifulSoup(res.text,"html.parser")
print(soup)