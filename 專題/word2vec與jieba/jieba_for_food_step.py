#!/usr/bin/env python
# coding: utf-8

import os,json,jieba,csv
from multiprocessing import Pool,cpu_count

#先讀上來食譜步驟==>字典jieba斷詞==>再套用停止詞==>輸出txt

#連線mongo讀資料
mongo_db="test"
mongo_db_collection="food4"

#食譜資料夾位置
path=r"E:\BIG DATA下載\專題\爬蟲\venv\collction_freefood_11_23"
#清理完的食譜txt
path2=r"E:\BIG DATA下載\專題\爬蟲\venv\clean_json_list6.txt"
# #斷詞dict位置
# jieba.load_userdict(r"F:\資策會\專題\爬蟲\venv\dict_for_jieba\dict_all_keep.txt")
# #停止詞dict位置
# stop_word_path=r"F:\資策會\專題\爬蟲\venv\dict_for_jieba\other_people_stop.txt"
# #整理後txt存檔位置
# clean_for_w2v_path=r"F:\資策會\專題\爬蟲\venv\clean_for_w2v.txt"


def load_file_from_mongo(mongo_db,mongo_db_collection):
    collections = [str(mongo_db_collection)]
    try:
        read_categories = mongo_db[collections[0]].find()
        for i in read_categories:
            #return i
            print(i)
    except:
        print(sys.exc_info())
def read_data(path):
    with open(path2,"r",encoding="utf-8") as f:
        list_json=[]
        while True:
            line=f.readline()
            list_json.append(line)
        # content=f.read()
        #return list_json
        print(list_json)

#讀進所有json_food
def output_foodname_for_w2v(path2):
    read_data(path2)
    # content=content.replace("[","").replace("]","")
    # content_list=content.split(",")
    # for i in content_list:
    #     print(i)
    #list_for_food_name=[]
    #print(content_list)
    # for i in content:
    #     print(i)
        # s=""
        # recipe_name = d["recipe_name"]
        # s+=recipe_name
        # list_ingredients = d["ingredients"]
        # for i in list_ingredients:
        #     ingredient_names = i["ingredient_names"]
        #     s+=ingredient_names
         #去掉空行，一個食譜步驟放入一次
        #list_for_food_name.append(s.replace("\n",""))
    #return list_for_food_name
    #print(list_for_food_name)


# In[16]:


# 讀進所有json
def read_from_json_step():
    json_list = os.listdir(path)
    list_for_steps=[]
    for i in json_list:
        with open(path + "/" + i, "r", encoding="utf-8") as f:
            dic = f.read()
            d = json.loads(dic)
            list_steps = d["cooking_steps"]
            #結合每個步驟
            s=""
            for i in list_steps:
                step=i["methods"]
                s+=step
            #去掉空行，一個食譜步驟放入一次
            list_for_steps.append(s.replace("\n",""))
    return list_for_steps


# In[17]:


#jieba斷詞
def cut(list_for_every_food_steps,stop_word_path):
    context=""
    stop_list=stop_word(stop_word_path)
    for food_step in list_for_every_food_steps:
        food_step_cut=jieba.cut(food_step)
        for word in food_step_cut:
            if word not in stop_list:
                context+=word+" "
        context+="\n"+"\n"

    return context


# In[18]:


def stop_word(stop_word_path):
    #把停止詞從字典拉上來，放入list
    stop_list=[]
    with open(stop_word_path,"r",encoding="utf-8") as f:
        for i in f.readlines():
            stop_list.append(i.replace("\n",""))
    return stop_list


# In[19]:


def context_to_txt(context):
    print(context)
    with open(clean_for_w2v_path,"w+",encoding="utf-8") as f:
        f.write(context)


# In[4]:


if __name__ == "__main__":
    #load_file_from_mongo(mongo_db,mongo_db_collection)
    output_foodname_for_w2v(path2)
    #read_from_json_food()
#     list_for_every_food_steps=read_from_json_step()
#     context=cut(list_for_every_food_steps,stop_word_path)
#     context_to_txt(context)



