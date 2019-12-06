import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue() #開一個queu
    p1 = mp.Process(target=job,args=(q,)) #參數只有一個 後面要逗號
    p2 = mp.Process(target=job,args=(q,))
    #看似一個queue 拿給兩個人 分別做同一件事 做完放進去 之後再拿出來 不會重複做嗎? 居然達到分工??
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get() #從queue拿出來
    res2 = q.get() #從queue拿出來
    print(res1+res2)