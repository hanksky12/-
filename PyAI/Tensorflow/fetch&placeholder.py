#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[4]:


#fetch多個OP執行
input1=tf.constant(3.0)
input2=tf.constant(2.0)
input3=tf.constant(5.0)

add=tf.add(input2,input3)
mul=tf.multiply(input1,add)

with tf.Session() as sess:
    result=sess.run([mul,add])#同時執行兩個OP，要[]
    print(result)


# In[5]:


#先用placeholder佔住位置"""必須"""搭配feed在run的時候再給數字
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)
output=tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.0],input2:[2.]}))#以字典方式給值


# In[ ]:




