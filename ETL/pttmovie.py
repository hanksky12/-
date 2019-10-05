import requests
from bs4 import BeautifulSoup
import os

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
headers = {'User-Agent' : useragent}

path = r'./res'
if not os.path.exists(path):
    os.mkdir(path)

page_number = 8317

while page_number > 8312:
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page_number)

    res = requests.get(url, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div[class="title"]')

    # print(title)
    for n, tmp_title in enumerate(title):
        try:
            print(tmp_title.a.text)
            article_url = 'https://www.ptt.cc' + tmp_title.a['href']
            print(article_url)
            # 再進行一次request
            res_article = requests.get(article_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, 'html.parser')
            article_content = soup_article.select('div[id="main-content"]')
            article_str = article_content[0].text.split('--')[0]
            with open('%s/%s.txt'%(path, tmp_title.a.text.replace('/', '-')), 'w', encoding='utf-8') as f:
                f.write(article_str)
            # print(article_str)
            print()
        except AttributeError as e:
            print('=========')
            print(e.args)
            print('=========')

    page_number -= 1