import MySQLdb
#12/14
word=""

g="100"
word1="盒"
word2=""

word3_list=[""]
#word3_list=["份","球","綑","把"]
#word3_list=["支","條","根","個","顆","枝","棵","朵","株"]
#word3_list=["粒","顆","個"]
#word3_list=["份","","盒"]
#word3_list=["條","塊","片","個"]
#word3_list=["塊","支","個","隻","支","根"]
#word3_list=["條","支","個","隻","尾"]
ID="J21901"
#細部調整
name=''

# def sql_transform_unitfc_to_number():
#     query = "select * from ingredient_unit_combine_update "
#     cursor.execute(query)
#     datarows=cursor.fetchall()
#     for row in datarows:
#             try:
#                 list(row)[2]=float(list(row)[2])
#             except ValueError as e:
#                  list(row)[2]=0
#             except TypeError as e:
#                  print(e)
#             print(list(row))

def sql_query(query):
    cursor.execute(query)
    datarows=cursor.fetchall()
    for row in datarows:
        print(row)

def update_to_sql(sql_update):
    cursor.execute(sql_update)

#將常用單位轉成字串
def make_input_words_with_synonym_unit_by_diff_foodtype(word3_list):
    word3=""
    for i in word3_list:
        word3 += "," + "\'" + i + "\'"
    return word3

#第0步:更改成可寫入
def step_0():
    change_safe_update = 'SET SQL_SAFE_UPDATES=0;'
    update_to_sql(change_safe_update)

#第一步 不依附食材的單位，一次做跨食材的轉換
def step_1(g,word):
    update_weight = 'update ingredient_unit_combine_update set unit_fc={}  where unit_overall=\'{}\' ;'.format(g, word)
    query = "select * from ingredient_unit_combine_update where unit_overall=\'{}\'".format(word)
    update_to_sql(update_weight)
    sql_query(query)
    #附加 轉換英文單位成小寫
    update_word_to_sql = 'update ingredient_unit_combine_update set unit_overall=\'{}\' where unit_overall=\'{}\' ;'.format(
        word.lower(), word)
    #update_to_sql(update_word_to_sql)

#第二步 依同意詞食材，用DATA食材ID，一次做跨食材的同意單位轉換，兩表join
def  step_2(g,ID,word1,word2,word3_list,name):
    word3 = make_input_words_with_synonym_unit_by_diff_foodtype(word3_list)
    #同時更新多單位,SQL裡面in後面""是空的沒問題(or的想法)
    word="\'"+word1+"\'"+","+"\'"+word2+"\'"+word3
    #print(word)
    #特別指定食材(細部調整)，SQL裡面where 條件有指定欄位就必須有值，不能指定為空，否則抓不到
    if name == "":
        name_word=name
    else:
        name_word="and name="+"\'"+name+"\'"
    update_weight= 'update ingredient_unit_combine_update  join equivalent_ingredients_name  on 1118_ingredient=name\
     set unit_fc={}  where ID=\'{}\' {} and unit_overall in ({});'.format(
        g,ID,name_word,word)
    query= 'select ID,name,unit_overall,unit_fc from ingredient_unit_combine_update join equivalent_ingredients_name\
     on 1118_ingredient=name where ID=\'{}\' {} and unit_overall in ({});'.format(ID,name_word,word)
    update_to_sql(update_weight)
    sql_query(query)


def main(g,word,ID,word1,word2,word3_list,name):
    #step_0()
    #step_1(g,word)
    step_2(g,ID,word1,word2,word3_list,name)

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user="hanksky", passwd="mindyiloveyou", db="free_food", port=3306, charset="utf8")
    cursor = db.cursor()  # 建立游標
    db.autocommit(True)  # 設定自動確認
    main(g,word,ID,word1,word2,word3_list,name)
    db.close()

