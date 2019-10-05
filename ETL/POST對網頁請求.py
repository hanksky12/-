from urllib import parse
from urllib import request
import requests

head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headers={"user-agent":"head"}
url="http://e2c87555.ngrok.io/hello_post"
post_data={"username":"sky"}

#用urllib
# data=bytes(parse.urlencode(post_data),encoding="utf-8")
# req=request.Request(url,headers=headers,data=data)
# res=request.urlopen(req)
# print(res.read().decode("utf-8"))

#用requests
res=requests.post(url,headers=headers,data=post_data)  #不是用requests.get 依網頁是不是post決定
print(res.text)

