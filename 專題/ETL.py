import pandas as pd
import os,json,re
path=r".\collction_freefood_11_23"
#讀所有json
json_list=os.listdir(path)

for i in json_list:
    try:
        with open(path + "/" + i, "r", encoding="utf-8") as f:
            try:
                dic = f.read()
                d = json.loads(dic)
                # print(d)
                #清理食材
                list_ingredients = d["ingredients"]
                # print(list_ingredients)
                for i in list_ingredients:
                    ingredient_names = i["ingredient_names"]
                    a=ingredient_names.replace("半", "0.5")
                    b=re.split(r"\d", a)[0]
                    c=re.sub(r"([^\u4e00-\u9fa5\u0041-\u005A\u0061-\u007A]|一(包|碗|小碗|附)|(適|少)(量|當|許)|新鮮|市售|\
                    |隔夜|切(段|絲|成|塊|片|碎末|花|碎|小丁|丁|末|細|條|小(塊|段))|約|(或|可(不用|用|依|選|均勻|不加|視家裡|替換|\
                    |省略|切分|以)).*)|(皆|亦|即|也|均)可|(此次|一(個|支|大匙|小(撮|匙)|隻|把)|(依|視)個人|又(稱|名)).*|\
                    |兩(?!節|層).*|數.*|少|個人包|成分|手切|去(皮|骨)|帶皮|現炒|原味|吃剩的|一(?!即|般)|小$.*|斜段","", b)
                    d=re.sub(r"各$|各(式|種)|片狀|特級冷壓初榨|剝殼|方便製作的份量|不同|小(丁|束)|酌量|茄子重量的|沒餡","",c)
                    #print(d)




                    list_ingredient_units=["適量","少許","一大匙","一小匙","一小撮","一包","酌量","少量","一把","一棵","一付"\
                                           ]
                    ingredient_units=i["ingredient_units"]
                    ingredient_units = ingredient_units.replace("半", "0.5")

                    for  n,j in enumerate(list_ingredient_units):
                        ingredient_units=ingredient_units.replace(str(j),str(n+10000))
                    print(d,"            ",ingredient_units)



            except ValueError as e:
                print(e)
            except JSONDecodeError as e:
                print(e)
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)






