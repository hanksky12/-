#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
import numpy as np


# In[4]:


#陣列的feed 
tf_placehold=tf.placeholder(tf.int32,shape=(3,))#3*1
with tf.Session() as sess:
    luck_number=sess.run(tf_placehold,{tf_placehold:[7,14,21]})#只有一個值要feed,可省feed_dict=
    print(luck_number)


# In[ ]:




