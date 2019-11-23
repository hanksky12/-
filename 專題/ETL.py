#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import os,json,re
path=r"F:\資策會\專題\爬蟲\venv\collctions"
#讀所有json
json_list=os.listdir(path)
json_list


# In[26]:


df=pd.DataFrame(columns=["食譜名稱","食材與單位","步驟"])
df


# In[27]:


for i in json_list:
    try:
        with open(path+"/"+i, "r", encoding="utf-8") as f:
            try:
        
                dic=f.read()
                d=json.loads(dic)
                food_list=[[]]
                food_list[0].append(d["recipe_name"])
                food_list[0].append(d["ingredients"])
                food_list[0].append(d["cooking_steps"])
                print(food_list)
                df=df.append(pd.DataFrame(food_list,columns=["食譜名稱","食材與單位","步驟"]))
            except ValueError as e:
                print(e)
            #except JSONDecodeError as e:
                #print(e)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)

        


# In[ ]:





# In[ ]:


def column_filter(s):
    #x= re.split('【|】|▪|：|•',s)[-1]
    x=s.replace("✿","")
    
    return x


# In[ ]:


try:
    df=df["食譜名稱"].apply(column_filter)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except AttributeError as e:
    print(e)
df


# In[24]:


df.to_csv(r'./icook.csv',index=0,encoding="utf-8")


# In[ ]:





# In[28]:


ddf=pd.DataFrame(columns=["食譜名稱","食材與單位"])
ddf


# In[29]:



foodd_list=[["陳皮紅豆湯圓x","[{'ingredient_names': '雞蛋蛋黃3顆', 'ingredient_units': '雞蛋蛋黃3顆'}]"],["花生x","[{'ingredient_names': '芝麻油10g', 'ingredient_units': '芝麻油10g'}]"]]
ddf=ddf.append(pd.DataFrame(foodd_list,columns=["食譜名稱","食材與單位"]))
ddf


# In[30]:


def column_filter(s):
    #x= re.split('【|】|▪|：|•',s)[-1]
    x=s.replace("✿","")
    
    return x


# In[82]:


for i in json_list:
    try:
        with open(path+"/"+i, "r", encoding="utf-8") as f:
            try:
        
                dic=f.read()
                d=json.loads(dic)
                #print(d)
                list_ingredients=d["ingredients"]
                #print(list_ingredients)
                for i in list_ingredients:
                    ingredient_names=i["ingredient_names"]
                    #print(ingredient_names)
                    a=re.split(r"\d",ingredient_names)[0].strip().split("（")[0].replace("少許","").replace("適量","").replace("少量","").replace("半","0.5")
                    b=re.split(r"\d",a)[0].replace("依個人喜好添加","").replace("適當","").strip().split("、")[0].split("﹙")[0].split("(")[0]                    .replace("新鮮","").replace("手工","").split("或")[0].replace("基底","").split("約")[0]
                    print(b)

                    
                
            except ValueError as e:
                print(e)
            except JSONDecodeError as e:
                print(e)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


# In[ ]:




