#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


luck_number=tf.Variable(24,name="luck_number")
with tf.Session() as sess:
    sess.run(luck_number.initializer)#只針對該變數初始化，不是全部喔!!
    print(sess.run(luck_number))


# In[ ]:




