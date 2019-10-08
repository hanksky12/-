#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt   


# In[2]:


# 使用 numpy 生成200個隨機點
x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]   # 產生一個二維數據
noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data) + noise

#定義兩個 placeholder
x = tf.placeholder(tf.float32,[None,1])     #   列不確定, 行為一行
y = tf.placeholder(tf.float32,[None,1])

#定義神經網路中間層 (十個神經元)
Weights_L1 = tf.Variable(tf.random_normal([1,10]))     # 輸入層一個神經元, 第二層有十個神經元
biases_L1 = tf.Variable(tf.zeros([1,10]))
Wx_plus_b_L1 = tf.matmul(x,Weights_L1) + biases_L1     # X:矩陣  Weights_L1: 矩陣
L1 = tf.nn.tanh(Wx_plus_b_L1)    # 雙曲正切函數（tanh）(激活函數)

# 定義神經網路輸出層 (一個神經元)
Weights_L2 = tf.Variable(tf.random_normal([10,1]))    
biases_L2 = tf.Variable(tf.zeros([1,1]))
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)    #預測結果

# 二次代價函數
loss = tf.reduce_mean(tf.square(y - prediction))
# 使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):   # 訓練兩千次
        sess.run(train_step,feed_dict = {x:x_data,y:y_data})  #訓練得傳入值為 feed_dict樣本點 (feed_dict是一個字典)
        
    #獲得預測值
    prediction_value = sess.run(prediction,feed_dict = {x:x_data}) #  傳入  x_data 得到預測值
    # 繪圖
    plt.figure()
    plt.scatter(x_data,y_data)    # 散點圖
    plt.plot(x_data,prediction_value,'r-',lw = 5)  # 畫折線圖
    plt.show()


# In[ ]:




