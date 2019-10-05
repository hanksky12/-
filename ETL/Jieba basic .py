#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install jieba')


# In[2]:


import jieba


# In[4]:


s="大家好，我很姬芭，今天外面下雨，心情不好，感覺真的很不爽"
s1=jieba.cut(s,cut_all=True)
s2=jieba.cut(s,cut_all=False)
s3=jieba.cut_for_search(s)
print("全模式","|".join(s1))
print()
print("精確模式","|".join(s2))
print()
print("搜尋引擎","|".join(s3))


# In[7]:


s4=jieba.cut(s)   #大家常用 不太會去選模式
print("簡單模式","|".join(s4))


# In[14]:


jieba.load_userdict("./mydict.txt")
s4=jieba.cut(s)   #大家常用 不太會去選模式
print("簡單模式","|".join(s4))


# In[20]:


stopword_list=[]
with open(r"./stopword.txt","r",encoding="utf-8" ) as f:
    for w in f.readline():
        stopword_list.append(w)
stopword_list #黑名單進來後 自己想程式去除


# In[ ]:





# In[ ]:




