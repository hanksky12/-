#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 導入 tensorflow
import tensorflow as tf   


# In[2]:


# 定義一個變量
x = tf.Variable([1,2])
# 定義一個常量
a = tf.constant([3,3])
# 增加一個減法 op
sub = tf.subtract(x,a)
# 增加一個加法 op
add = tf.add(x,sub)
# 初始化變量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))


# In[3]:


# 創建一個變量初始化為 0
state = tf.Variable(0,name = 'counter')
#創建一個 op, 作用是使 state 加一
new_value = tf.add(state,1)
#賦值 (new_value  設定給  state)
update = tf.assign(state, new_value)
#變量初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print( sess.run(state))


# In[ ]:




