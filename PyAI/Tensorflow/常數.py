#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
print(tf.__version__)


# In[2]:


m1=tf.constant([[3,3]])#1*2matrix
m2=tf.constant([[2],[3]])#2*1matrix
product=tf.matmul(m1,m2)#matrix 乘積==>這是一個operation
print(product)#矩陣1*1===>這邊值沒有出來 被存在tensor裡面


# In[3]:


sess=tf.Session()
result=sess.run(product)
print(result)


# In[ ]:




