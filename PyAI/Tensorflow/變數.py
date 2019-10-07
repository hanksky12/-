#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf


# In[3]:


x=tf.Variable([1,2])
y=tf.Variable([3,3])
sub=tf.subtract(x,y) #op
add=tf.add(sub,x) #op

init=tf.global_variables_initializer()#op 給他個名字 有變數的圖 執行前要先(初始化:對變數設值，)
with tf.Session() as sess:
    sess.run(init)#圖有變數要先init
    print(sess.run(sub))#跑圖
    print(sess.run(add))#跑圖


# In[4]:


state=tf.Variable(0,name="counter")
new_value=tf.add(state,1)
update=tf.assign(state,new_value)#把new_value指派給state

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    sess.run(update)
    print(sess.run(update))


# In[7]:


state=tf.Variable(0,name="counter") #變數
new_value=tf.add(state,1) #OP
update=tf.assign(state,new_value)#OP      把new_value指派給state 

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())##初始化可以拉進來
    print(sess.run(state))
    for _ in range(5):##跑個五次
        sess.run(update)
        print(sess.run(state))


# In[ ]:




