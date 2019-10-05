import requests
from bs4 import BeautifulSoup
import os
import time
# user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
# head={"user-agent":user_agent}
# ss=requests.session()
# ss.cookies["DIS_MODE"]="1"
path=r'./BUG104'
if not os.path.exists(path):
    os.mkdir(path)

page_number=1
while page_number>=1:
    urlll=r"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%s&order=1&asc=0&page=%s&mode=l&jobsource=2018indexpoc"%("Python",page_number)
    res=requests.get(urlll)
    soup=BeautifulSoup(res.text,"html.parser")
    every_link=soup.select("li[class='job-mode__jobname']")
    #print(every_link)

    for i in every_link:
        try:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            in_url="http://"+i.a['href'].lstrip("/")
            #print("http://"+i.a['href'].lstrip("/"))
            in_res = requests.get(url=in_url)
            in_soup = BeautifulSoup(in_res.text, "html.parser")
            in_job=in_soup.select('div[class ="center"]')
            in_content=in_soup.select('div[class ="content"]')
            in_paper=''
            for j in in_job:
                in_job_name=j.h1.text.strip().split("\n")[0].strip()
                in_company_name=j.h1.text.strip().split("\n")[1].strip()
            #print(type(in_content))
            in_person=str(in_content[1].dl.text.strip().split("聯絡方式")).replace(r"\n","").replace(r"\r","")  #測試用 "聯絡方式"可以完美分隔  上半的條件:XXX 和下半聯絡:XXXX  再轉字串最後用replace取代文字裡面的\r 跟\n
            in_mail=str(in_content[3].dl.text.strip().split("聯絡方式")).replace(r"\n","").replace(r"\r","")  #一個剛好在[1]一個在[3]
            in_jog_do = str(in_content[0].p.text.split("公司福利")).replace(r"\r","").replace(r"\t","")
            print(in_url)
            print(in_mail)
            # for i in in_content:
            # #in_jog_welfare = in_content.p.text.strip("公司福利")
            #     print(i.in_jog_do)


        except TypeError as e:
            print(e)
        except AttributeError as e:
            print(e)
    page_number -= 1