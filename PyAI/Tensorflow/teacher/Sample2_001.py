#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 導入 tensorflow
import tensorflow as tf   


# In[2]:


#  創建一個常量  op
m1 = tf.constant([[3,3]])
#  創建一個常量  op
m2 = tf.constant([[2],[3]])
#   創建一個矩陣乘法 op,   把 m1 和 m2  傳入
product = tf.matmul(m1,m2)
print(product)


# In[10]:


# 定義一個會話 , 啟動默認圖
sess = tf.Session()
#  調用 sess  的  run  方法來執行矩陣乘法 op
#  run(product) 觸發了圖中的 3 個 op
result = sess.run(product)
print(result)
#  關閉會話 ,釋放資源
sess.close()


# In[6]:


with tf.Session() as sess:
    #   調用 sess  的  run  方法來執行矩陣乘法 op
    #   run(product) 觸發了圖中的 3 個 op
    result = sess.run(product)
    print(result)    


# In[ ]:





# In[ ]:




