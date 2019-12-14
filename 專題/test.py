import MySQLdb

sql_str = "select * from ingredient_unit_combine_update"  # select語法
def sql_query(sql_str):
    try:
        cursor.execute(sql_str)
        datarows=cursor.fetchall()
        data_list=[]
        for row in datarows:
            data_list.append(list(row))
        return data_list
    except:
        print("無法連接db")


def tran(data_list):
    for row_list in data_list:
         if row_list[2]=="滴":
             print(row_list)


#def main(sql_str):




if __name__=="__main__":
    db = MySQLdb.connect(host="36.228.69.179", user="user", passwd="user", db="iii_project", port=3306, charset="utf8")
    cursor = db.cursor()  # 建立游標
    data_list=sql_query(sql_str)
    tran(data_list)
    db.close()

