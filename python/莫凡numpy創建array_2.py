import numpy as np
#一維
a=np.array([2,23,4],dtype=np.int)
#觀察印出來的矩陣沒有逗號
print(a)
#我的默認int32 float64 設越多空間占用大但是越準
print(a.dtype)

#2維
b=np.array([[1,2,3],[4,5,6]])
print(b)

#全部是0  指定shape
c=np.zeros((3,4),dtype=np.float64)
print(c)

#全部是1  指定shape
d=np.ones((2,5),dtype=np.int8)
print(d)

#empty 接近為0的matrix
e=np.empty((3,3))
print(e)

#每隔2介於10~20的數字，生成的matrix
f=np.arange(10,20,2)
print(f)

#將矩陣 重新做形狀
g=np.arange(12).reshape((3,4))
print(g)

#將10-3的距離=7，平分成5-1段==>每7/4得到一個數字
#3到10的中間距離，平均分成4段，取數字
h=np.linspace(3,10,5)
print(h)