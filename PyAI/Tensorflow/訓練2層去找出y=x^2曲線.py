#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# In[15]:


#製造一推類似y=x^2的點分布圖 
x_data=np.linspace(-0.5,0.5,200)[:,np.newaxis]#200的隨機點在-0.5到0.5 #np.newaxis 維度未知  200列 不知多少行
noise=np.random.normal(0,0.02,x_data.shape)#產生隨機點平均是0標準差0.02 形狀和x_data依樣
y_data=np.square(x_data)+noise #如果不加noise 就是y=x^2 

#照片的圖跟這邊矩陣不太依樣 
#############目標 讓模型去找一條曲線符合分布圖，這條線就是y=x^2
x=tf.placeholder(tf.float32,[None,1])#列未知 行1 
y=tf.placeholder(tf.float32,[None,1])#列未知 行1   newaxis = None

Weight_L1=tf.Variable(tf.random_normal([1,10]))  #第一層權重  第一次權重不能給0
biases_L1=tf.Variable(tf.random_normal([1,10]))  #第一層偏移  也可以用給0 tf.zeros([1,10])
Wx_plus_b_L1=tf.matmul(x,Weight_L1)+biases_L1    #1*1 mat 1*10==>1*10+ 1*10==>1*10
L1=tf.nn.tanh(Wx_plus_b_L1)  #第一層經過激勵函數 O

Weight_L2=tf.Variable(tf.random_normal([10,1]))  #第二層權重
biases_L2=tf.Variable(tf.random_normal([1,1]))  #第二層偏移
Wx_plus_b_L2=tf.matmul(L1,Weight_L2)+biases_L2    #用前面的L1 1*10進來 1*10 mat 10*1==>1*1+1*1==>1*1
prediction=tf.nn.tanh(Wx_plus_b_L2)  #預測值


#損失函數
loss=tf.reduce_mean(tf.square(y-prediction)) #真實y(200個值)減掉預測y(200個值) 平方後取平均
#訓練函數(用梯度下降法)來訓練:     使loss變小   0.1是學習率 越小學越慢越精細 
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)


#訓練流程:餵x,y經過網路，算出損失函數回饋W跟B給每一層
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):#每訓練一次完 x,y都是再餵一次
        sess.run(train_step,feed_dict={x:x_data,y:y_data}) ###餵進來當下 x固定為200*1 y也是
        
    
    ####畫圖(用200個點的連線)
    prediction_value=sess.run(prediction,feed_dict={x:x_data})#去抓出最後一次預測的y
    plt.figure()
    plt.scatter(x_data,y_data)#用scatter:散點圖 畫出真實值
    plt.plot(x_data,prediction_value,"r-",lw=5)#用plot:折線圖，x座標用原DATA y座標用預測的y  紅色線段 寬度=5
    plt.show()


# In[ ]:




