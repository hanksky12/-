#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# In[2]:


# 載入數據集 (放在當前工作路徑)
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

# 每個批次的大小 (一次放一百張圖片進去訓練)
batch_size = 100
# 計算一共有多少個批次
n_batch = mnist.train.num_examples // batch_size

#定義兩個 placeholder
x = tf.placeholder(tf.float32,[None,784]) # 圖像输入向量 (28x28 = 784)   
y = tf.placeholder(tf.float32,[None,10])  # 10個標籤

# 創建一個簡單的神經網路 (兩個層: 輸入層與輸出層)
W = tf.Variable(tf.zeros([784,10]))  # 權重，初始化值為全零  ( 輸入層780 個神經元,輸出層 :十個神經元)
b = tf.Variable(tf.zeros([10]))      # 偏置，初始化值為全零  
# 實現我們的模型
prediction = tf.nn.softmax(tf.matmul(x,W)+b)

#定義二次代價函數
loss = tf.reduce_mean(tf.square(y-prediction))
# 使用梯度下降法 (使用BP算法來進行微調,以0.2的學習速率 )
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化變量
init = tf.global_variables_initializer()

#結果存放在一個布林型態的列表中 (判断預测標籤和實際標籤是否匹配)
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))  #argmax  返回一維張量中最大的值所在的位置
#求準確率 (把布林值轉換成浮點數)
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
# 啟動創建的模型，並初始化變量
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):   #  疊代 21 次
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # batch_xs :  圖片數據   batch_ys:  圖片標籤
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        # 計算所學習到的模型在测試數據集上面的正確率   
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter"+str(epoch)+", Testing Accuracy :"+str(acc))


# In[ ]:





# In[ ]:




