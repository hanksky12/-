#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os,json,re
path=r"F:\資策會\專題\爬蟲\venv\res"
#讀所有json
json_list=os.listdir(path)
json_list


# In[2]:


df=pd.DataFrame(columns=["檔名","食譜名稱","食材與單位","步驟"])
df


# In[12]:


for i in json_list:
    try:
        with open(path+"/"+i, "r", encoding="utf-8") as f:
            try:
        
                dic=f.read()
                d=json.loads(dic)
                food_list=[]
                food_list.append(d["recipe_name"])
                food_list.append(d["quantity"])
                #print(food_list)
                df=df.append(pd.DataFrame(food_list,columns=["檔名","份數"]))
            except ValueError as e:
                print(e)
            except JSONDecodeError as e:
                print(e)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)

        


# In[ ]:





# In[ ]:


def column_filter(s):
    #x= re.split('【|】|▪|：|•',s)[-1]
    x=s.replace("］","")
    
    return x


# In[ ]:


try:
    df=df["食譜名稱"].apply(column_filter)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
df


# In[11]:


df.to_csv(r'./bbb.csv',index=0,encoding="utf-8")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




