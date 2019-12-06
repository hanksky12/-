import multiprocessing as mp
#處理單值
value1 = mp.Value('i', 0) #signed int
value2 = mp.Value('d', 3.14) # double  (float)
#處理限定1維array
array = mp.Array('i', [1, 2, 3, 4])


#https://docs.python.org/3/library/array.html  參數參考