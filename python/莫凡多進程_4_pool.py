import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool() #自動找電腦核心數
    res = pool.map(job, range(10)) #參數可多個 ，多核
    print(res)

    res = pool.apply_async(job, (2,)) #參數限定一個，單核
    # 用get获得结果
    print(res.get())
    #硬要跑多參數 在單核
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])

if __name__=='__main__':
    multicore()