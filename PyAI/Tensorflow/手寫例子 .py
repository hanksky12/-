#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# In[8]:


mnist = input_data.read_data_sets("MNIST_data",one_hot=True) #將下載的東西放到MNIST資料夾

# 每個批次的大小 (一次放一百張圖片進去訓練)
batch_size = 100
# 計算一共有多少個批次
n_batch = mnist.train.num_examples // batch_size

#定義兩個 placeholder 原始資料
x = tf.placeholder(tf.float32,[None,784]) # 圖像输入向量 (28x28 = 784)   matrix:列*784
y = tf.placeholder(tf.float32,[None,10])  # 已經標好的標籤                    matrix:列*10


# 創建一個簡單的神經網路 (兩個層: 輸入層與輸出層)沒有隱藏層
W = tf.Variable(tf.zeros([784,10]))  # 權重，初始化值為全零  ( 輸入層780 個神經元,輸出層 :十個神經元)
b = tf.Variable(tf.zeros([10]))      # 偏置，初始化值為全零  10個
# 實現我們的模型
prediction = tf.nn.softmax(tf.matmul(x,W)+b) #預測值y  以矩陣1*10 每個都是機率<1 加起來=1 

#定義二次代價函數(損失函數)
loss = tf.reduce_mean(tf.square(y-prediction))
# 使用梯度下降法 (使用BP算法來進行微調,以0.2的學習速率 )
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#初始化變量
init = tf.global_variables_initializer()


######算正確率
#結果存放在一個布林型態的列表中 (判断預测標籤和實際標籤是否匹配)
#argmax  找出矩陣最大的值設成1，其他為0  對預測的y就是將機率大的那一格轉成1 真實labels轉換後一樣  將真實y與預測y比對 返回TRUE or FAULE
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))  
#正確率 (把布林值轉換成浮點數)     用cast函數將BOOL轉浮點數 再算平均
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))



# 啟動創建的模型，並初始化變量
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):   #  疊代 21 次
        # 給100圖返回 100圖 跟 100個標籤
        for batch in range(n_batch):  #共10000/100=10批次 不用他給的函數要自己寫標籤
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)  # 將真實值 batch_xs:圖片數據  和相對應的batch_ys:圖片標籤 ==>放進去讓prediction能越來越接近真實數據的標籤
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})   
        # 計算所學習到的模型在测試數據集上面的正確率   
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})#餵原始圖 跟 已經轉好的y labels
        print("Iter"+str(epoch)+", Testing Accuracy :"+str(acc))


# In[6]:


mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels
print(x_test.shape)
print(y_test)


# In[ ]:




