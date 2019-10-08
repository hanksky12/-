#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np


# In[2]:


# 使用 numpy 生成100個隨機點
x_data = np.random.rand(100)
y_data = x_data*0.1 + 0.2

# 構造一個線性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

# 二次代價函數 (我們的目標是要讓 loss（MSE）最小化)
loss = tf.reduce_mean(tf.square(y_data-y))
#定義一個梯度下降法來進行訓練的優化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
# 最小化代價函數
train = optimizer.minimize(loss)

# 初始化變量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step%20 == 0:   # 每跑 20 次把當時的係數與截距印出來
            print(step,sess.run([k,b]))


# In[ ]:





# In[ ]:




