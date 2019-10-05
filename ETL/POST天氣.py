import requests

head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
headers={"user-agent":"head"}
url="http://e2c87555.ngrok.io/weather"
post_data={"location":"台中"}

res=requests.post(url,headers=headers,data=post_data)
print(res.text)

