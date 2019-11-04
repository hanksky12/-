from bs4 import BeautifulSoup
import multiprocessing as mp
import os,time,random,requests



def lazy(human):
    t0 = time.time()
    print("start")
    queue=mp.JoinableQueue()
    for i in range(human+1):
        worker_i=mp.Process(target=worker,args=(i+1,queue))
        worker_i.daemon=True
        worker_i.start()
        print(worker_i)
    producer(queue)
    queue.join()
    print(time.time()-t0, "seconds time")