#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[56]:


source_path=r"./homework1.2/"
file_list=os.listdir(source_path)


# In[57]:


df_list = [] #為了符合df.append格式要有大list
for article in file_list:
    with open(source_path+"/"+article,"r",encoding="utf-8") as f:
              tem_str=f.read()
    #print(tem_str)
    try:
        info_list = tem_str.split("~~~~~~~~~~split~~~~~~~~~~~~~")[1].split("\n")[1:-1]  #每一個都是小list
    except IndexError:
        print("e.args")
    df_list.append(info_list)
    #print(info_list)
    print(df_list)
    


# In[58]:


df=pd.DataFrame(columns=["推","噓","分數","作者","時間","標題"])
df


# In[37]:


new_df=pd.DataFrame(df_list,columns=["推","噓","分數","作者","時間","標題"])
new_df


# In[59]:


df=df.append(new_df)
df


# In[60]:


def column_filter(tmpstr):
    return tmpstr.split(":")[1]


# In[42]:


df["推"].apply(column_filter)


# In[61]:


df["推"]=df["推"].apply(column_filter)
df


# In[63]:


df_back=df  #用過濾器之前 記得先備份
df


# In[77]:


#print(df[1])   df[1] not list

for c in df[columns[0:3]]:
    print(c)
    try:
        df[c]=df[c].apply(column_filter)
    except IndexError:
        print("@@@@@@@@@@@@@@@@")


# In[78]:


df


# In[53]:


new_df["推"].apply(lambda s:s.split(":")[1])


# In[75]:


columns=["推","噓","分數","作者","時間","標題"]#這裡是list  對python 的基本功不夠
columns[0:2]
df[columns[0:3]]#所以在過濾指定的多欄位時，可以用這邊的index


# In[ ]:




