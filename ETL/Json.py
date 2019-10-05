# import requests
import json
from urllib import request
import os
# url="https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232063592"
# head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
# headers={"user-agent":head}
# res=requests.get(url,headers=headers)
# tmp_json=json.loads(res.text)
photo_path=r"/photo"
if not os.path.exists(photo_path):
    os.mkdir(photo_path)
with open("./json1.txt","r",encoding="utf-8") as f:
    tmp_json=f.read()
#print(tmp_json)
js_dict=json.loads(tmp_json)# 用套件裡面的loasds 把文件丟進去
#print(type(js_dict)) #一個很大的list 包含多部字典
#for i in js_dict:  #出來有多個字典
    #print(i)
#print(js_dict[0]) #選第0個
# for j in js_dict[0]: #第0部字典的所有KEY
#      print(j)
#print(js_dict[0]['mediaMeta'])
for i in js_dict:
    print(i["title"])
    print("https://www.dcard.tw/f/photography/p"+str(i["id"]))
    for n,j in enumerate(i['mediaMeta']):
        try:
            photo_url=j["url"]
            print(photo_url)
            #套件urllib 裡面的request的urlretrieve可下載圖片 圖片路徑 檔名
            request.urlretrieve(photo_url,photo_path+"/%s%s.jpg"%(i["title"],n))
        except OSError:# 原檔名的問題造成系統 OSError
            print("@@@@@@@@@@@@@@@@@@@@@@")

