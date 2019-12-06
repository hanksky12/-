import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
print(a,b)

#矩陣+,-
c=a+b
print(c)

#矩陣平方
d=b**2
print(d)

#科學運算
e=10*np.cos(a)
print(e)

#判斷值 返回布林矩陣
print(b<3)
print(b==3)

#矩陣 * dot
z=np.array([[1,1],
           [0,1]])
x=np.arange(4).reshape((2,2))

y=z*x
y_dot=np.dot(z,x)
y_dot_2=z.dot(x)
print(y)
print(y_dot)
print(y_dot_2)

#隨機生成矩陣 指定shape
k=np.random.random((2,4))
print(k)

#矩陣元素加法，求元素最大、最小值，針對行或列
print(np.sum(k))
print(np.min(k))
print(np.max(k))
print("")
print(np.sum(k,axis=1))#對列
print(np.min(k,axis=0))#對行
print(np.max(k,axis=1))#對列