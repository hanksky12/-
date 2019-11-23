#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os,json,re
path=r"./collction"
#讀所有json
json_list=os.listdir(path)

df=pd.DataFrame(columns=["檔名","食譜時間","食材與單位","步驟"])

for i in json_list:
    try:
        with open(path+"/"+i, "r", encoding="utf-8") as f:
            try:
                dic=f.read()
                d=json.loads(dic)
                food_list=[[]]
                food_list[0].append(d["recipe_name"])
                #print(food_list)
                food_list[0].append(d["post_time"])
                #print(food_list)
                food_list[0].append(d["quantity"])
                #print(food_list)
                df=df.append(pd.DataFrame(food_list,columns=["檔名",'食譜時間','食材與單位']))
            except ValueError as e:
                print(e)
            except JSONDecodeError as e:
                print(e)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)

def column_filter(s):
    #x= re.split('【|】|▪|：|•',s)[-1]
    x=s.replace("］","")
    return x

# try:
#     df=df["食譜名稱"].apply(column_filter)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
print(df)
df.to_csv(r'./bbb.csv',index=0,encoding="utf-8")


