import pandas as pd
import MySQLdb,random

#user_id
n=2
#幾個推薦食譜
m=10

def sql_query(query):
    cursor.execute(query)
    datarows=cursor.fetchall()
    return datarows

def update_to_sql(sql_update):
    cursor.execute(sql_update)

#第0步:更改成可寫入
def step_0():
    change_safe_update = 'SET SQL_SAFE_UPDATES=0;'
    update_to_sql(change_safe_update)

#疊代相加
def plus(data_tag,n,m):
    #不寫會有ERROR，因為range(n,n)沒有東西
    if m==(n+1):
        return data_tag[n]
    else:
        for i in range(n, m - 1):
            data_tag[i + 1] = data_tag[i] + data_tag[i + 1]
            tmp = data_tag[i + 1]
        return tmp

#原始想法檢查
    # list_text_cluster_score=[plus(data_tag, 1, 3),plus(data_tag, 4, 6),plus(data_tag, 7, 8)]
    # list_nutrition_cluster_score=[plus(data_tag, 9, 9),plus(data_tag, 10, 11),plus(data_tag, 12, 13),plus(data_tag, 14, 17), \
    #                              plus(data_tag, 18, 18),plus(data_tag, 19, 19),plus(data_tag, 20, 22),plus(data_tag, 23, 23), \
    #                               plus(data_tag, 24, 24),plus(data_tag, 25, 26)]
def tag_compute(data_tag):
    point_list=[2,5,7,10,11,14,16,20,21,22,25,26,27,28]
    list_text_cluster_score=[]
    list_nutrition_cluster_score=[]
    for n,i in enumerate(point_list):
        #第一建模分3,3,2
        if i <9 :
            tmp=plus(data_tag, point_list[n], point_list[n + 1])
            list_text_cluster_score.append(tmp)
        #第二建模尾巴28當邊界用  所以不需要計算
        elif i >=9 and n<len(point_list)-1:
            tmp=plus(data_tag, point_list[n], point_list[n + 1])
            list_nutrition_cluster_score.append(tmp)
    text_cluster=list_text_cluster_score.index(max(list_text_cluster_score))+1
    nutrition_cluster=list_nutrition_cluster_score.index(max(list_nutrition_cluster_score))+1
    return text_cluster,nutrition_cluster

def step_1(n):
    query_1="select * from users_tags where user={}".format(n)
    datarows=sql_query(query_1)

    data_tag=list(list(datarows)[0])
    print(data_tag)
    text_cluster,nutrition_cluster=tag_compute(data_tag)
    query_2 = "select * from km_10_clusters where cluster={} and text_cluster={}".format(nutrition_cluster,text_cluster)
    datarow_2=sql_query(query_2)
    return datarow_2

def top_m(cluster_intersection,m):
    top10_tuple=random.sample(list(cluster_intersection),k=m)
    top10_df=pd.DataFrame(list(top10_tuple))
    print(top10_df)
    return list(top10_df.iloc[:,0])

def main(n,m):
    step_0()
    cluster_intersection=step_1(n)
    id_list=top_m(cluster_intersection,m)
    print(id_list)

if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="iii_project", port=3306, charset="utf8")
    cursor = db.cursor()  # 建立游標
    db.autocommit(True)  # 設定自動確認
    main(n,m)
    db.close()