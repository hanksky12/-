import multiprocessing as mp
import threading as td

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')
thread_2 = threading.Thread(target=T2_job, name='T2')
thread_1.start() # 开启T1
thread_2.start() # 开启T2
#這邊要去比較不開join 跟只開T1 或開T2  還有全開 的差別
thread_2.join() # join for T2
thread_1.join() # join for T1
print("all done\n")