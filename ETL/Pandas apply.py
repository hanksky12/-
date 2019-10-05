#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.DataFrame(columns=["name","age","hight"])
df


# In[3]:


df.loc[0]=["a","10","120"]
df


# In[4]:


df.loc[2]=["b","20","180"]
df


# In[6]:


df.loc[2]=["k","30","150"]
df


# In[8]:


df["name"]="g"
df


# In[10]:


df.to_csv(r"./test_panda.csv",index=0,encoding="utf-8")


# In[11]:


df2=pd.read_csv(r"./test_panda.csv")
df2


# In[12]:


new_df =pd.DataFrame([["A","22","175"],["B","25","190"]],columns=["name","age","hight"])
new_df


# In[13]:


df


# In[14]:


df.append(new_df)


# In[15]:


df


# In[17]:


df=df.append(new_df)
df


# In[ ]:




