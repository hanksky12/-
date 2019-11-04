from bs4 import BeautifulSoup
import multiprocessing as mp
import os,time,random,requests

headers={"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
"Connection": "keep-alive",
"Host": "r6---sn-ipoxu-u2xz.googlevideo.com",
"Origin": "https://www.youtube.com",
"Referer": "https://www.youtube.com/embed/9Dx61cOLjo4?autoplay=1&controls=1&showinfo=0&autohide=1&rel=0&hd=1&wmode=opaque&enablejsapi=1&origin=https%3A%2F%2Fwww.ytower.com.tw&widgetid=1",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "cross-site",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
"X-Client-Data": "CIi2yQEIpbbJAQjEtskBCKmdygEI4qjKAQjOsMoBCPe0ygEYq6TKAQ=="}

path=r'./food_young'  #資料夾
if not os.path.exists(path): #沒有這個資料夾就新創資料夾
    os.mkdir(path)




def first(queue):
    # 第一層
    url_first = "https://food.ltn.com.tw/category"
    res_first = requests.get(url_first, headers=headers)
    soup_first = BeautifulSoup(res_first.text, 'html.parser')
    # tag p包含我要的五穀雜糧、肉類..而且五穀雜糧下面的細項不點選就已經全在五穀頁面裡面，到下層連結只要用五穀雜糧就可抓到全部
    titles_first = soup_first.select('p')
    producer(titles_first,queue)

def main(human):
    t0 = time.time()
    print("start")
    queue=mp.JoinableQueue()
    for i in range(human+1):
        worker_i=mp.Process(target=worker,args=(i+1,queue))
        worker_i.daemon=True
        worker_i.start()
        print(worker_i)
    first(queue)
    queue.join()

if __name__ == "__main__":
    main(human) #worker數目