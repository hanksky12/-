import multiprocessing as mp
import threading as td

#這邊示範多進程 多線程寫法都一樣
def job(a,d):
    print('aaaaa')

if __name__=='__main__':
    t1 = td.Thread(target=job,args=(1,2)) #第一個放函數 第二個放要給函數的參數 這行只是設定
    p1 = mp.Process(target=job,args=(1,2))
    t1.start() #真的開始執行
    p1.start()
