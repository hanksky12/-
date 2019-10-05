from selenium.webdriver import Chrome
import requests

url="https://www.ptt.cc/bbs/index.html"
diver=Chrome("./chromedriver")
diver.get(url)
diver.find_element_by_class_name("board-name").click()
diver.find_element_by_class_name("btn-big").click()
print(diver.get_cookies())
diver.close()
ss=requests.session()
for i in cookie_list:
    ss.cookies.set(i["name"],i["value"])
res=ss.get("https://www.ptt.cc/bbs/index.html")
print(res.text)