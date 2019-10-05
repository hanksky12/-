#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import jieba


# In[3]:


source_path=r"./homework1.2/"
file_list=os.listdir(source_path)
print(file_list)


# In[7]:


article_str=""
for article in file_list:
     with open(source_path+"/"+article,"r",encoding="utf-8") as f:
            #把每篇文章全部串接再一起
            article_str+=f.read().split("~~~~~~~~~~split~~~~~~~~~~~~~")[0]
#print(article_str)


# In[9]:


new_str=article_str.replace("\n","")
s=jieba.cut(new_str)
#print(s)
word_count={}
for w in "|".join(s).split("|"):
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
word_count


# In[10]:


word_count_list=[]
for wc in word_count:
    word_count_list.append((wc,word_count[wc]))


# In[13]:


word_count_list.sort(key=lambda x : x[1] ,reverse=True)   
#list.sort(cmp=None, key=None, reverse=False)mp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
word_count_list


# In[ ]:




