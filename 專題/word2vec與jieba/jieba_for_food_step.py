#!/usr/bin/env python
# coding: utf-8

import os,json,jieba,csv
from multiprocessing import Pool,cpu_count

#先讀上來食譜步驟==>字典jieba斷詞==>再套用停止詞==>輸出txt
#連線mongo讀資料
mongo_db="test"
mongo_db_collection="food4"

#原始食譜資料夾位置
path=r"F:\資策會\專題\爬蟲\venv\collction_freefood_11_23"
#清理完的食譜txt
path2=r"F:\資策會\專題\爬蟲\venv\collction_freefood_clean"


#斷詞dict位置
jieba.load_userdict(r"F:\資策會\專題\爬蟲\venv\dict_for_jieba\dict_all_keep.txt")
#停止詞dict位置
stop_word_path=r"F:\資策會\專題\爬蟲\venv\dict_for_jieba\other_people_stop.txt"
#整理後txt給word2vec訓練用存檔位置
clean_for_train_w2v_path=r"F:\資策會\專題\爬蟲\venv\clean_for_w2v_0649.txt"
#整理後txt給換算食譜詞向量的存檔位置
clean_for_word_embedding_path=r"F:\資策會\專題\爬蟲\venv\clean_for_word_0649.txt"

def load_file_from_mongo(mongo_db,mongo_db_collection):
    collections = [str(mongo_db_collection)]
    try:
        read_categories = mongo_db[collections[0]].find()
        for i in read_categories:
            #return i
            print(i)
    except:
        print(sys.exc_info())

#讀進所有json_food
def read_from_json():
    json_list = os.listdir(path2)
    list_for_json=[]
    for i in json_list:
        with open(path2 + "/" + i, "r", encoding="utf-8") as f:
            dic = f.read()
            d = json.loads(dic)
            list_for_json.append(d)
    #print(list_for_json)
    return list_for_json

# 轉變成w2v符合的格式
def transform_step_to_w2v(list_for_json):
    list_for_steps=[]
    for d in list_for_json:
        list_steps = d["cooking_steps"]
        #結合每個步驟
        s=""
        for i in list_steps:
            step=i["methods"]
            s+=step
        #去掉空行，一個食譜步驟放入一次
        list_for_steps.append(s.replace("\n",""))
    return list_for_steps

# 轉變成w2v符合的格式
def transform_ingredient_names_to_w2v(list_for_json):
    #list_for_ingredient_names=[]
    s = ""
    for d in list_for_json:
        ingredients = d["ingredients"]

        for i in ingredients:
            name=i["ingredient_names"]
            s+=name+" "
        # list_for_ingredient_names.append(s)
        s+="\n"+"\n"
    return s

#jieba斷詞
def cut(list_for_every_food_steps):
    list_cut_step_every_food=[]
    context=""
    stop_list=stop_word()
    for food_step in list_for_every_food_steps:
        list_cut_step_one_food = []
        food_step_cut=jieba.cut(food_step)
        for word in food_step_cut:
            if word not in stop_list:
                list_cut_step_one_food.append(word)
                context+=word+" "
        list_cut_step_every_food.append(list_cut_step_one_food)
        context+="\n"+"\n"

    return context,list_cut_step_every_food


def stop_word():
    #把停止詞從字典拉上來，放入list
    stop_list=[]
    with open(stop_word_path,"r",encoding="utf-8") as f:
        for i in f.readlines():
            stop_list.append(i.replace("\n",""))
    return stop_list

def context_to_txt(context,list_cut_step_every_food):
    with open(clean_for_train_w2v_path,"w+",encoding="utf-8") as f:
        f.write(context)
    with open(clean_for_word_embedding_path,"w+",encoding="utf-8") as f:
        f.write(str(list_cut_step_every_food))

def ingredient_names():
    list_for_json = read_from_json()
    context = transform_ingredient_names_to_w2v(list_for_json)
    context_to_txt(context)


def step():
    list_for_json = read_from_json()
    list_for_every_food_steps = transform_step_to_w2v(list_for_json)
    context,list_cut_step_every_food=cut(list_for_every_food_steps)
    context_to_txt(context,list_cut_step_every_food)


if __name__ == "__main__":
    #ingredient_names()
    step()




