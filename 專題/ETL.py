import pandas as pd
import os,json,re,csv

path=r"E:\BIG DATA下載\專題\爬蟲\venv\collction_freefood_11_23"



# def trans(str,unicode_down,unicode_up):
#     for i in range(int("0x"+unicode_down,16),int("0x"+unicode_down,16)):
#         if ord(str)==i:
#             #將大寫數字轉成小寫數字，ord()可將字串轉成utf-8十進制整数 chr()則是反函數,觀察全形和半形差65248變可轉換 半形數字0-9
#             return chr(ord(str)-65248)
#         else:
#             pass
#
# trans("１","FF10","uFF19")
def split_ingredient_units_to_number(ingredient_units_clean):
    try:
        x=re.search(r"\d*.?\d",ingredient_units_clean)
        if x:
            number=x.group()
            return number+"xxxxx"
    except TypeError as e:
        print(e)



def split_ingredient_units_to_unit(ingredient_units_clean):
    try:
        x=re.search(r"[^0-9.]",ingredient_units_clean)
        if x:
            #print(x.group())
            unit=x.group()
            return unit
    except TypeError as e:
        print(e)
def csv_to_out(ingredient_names_clean,number,unit):
    with open('free_food_clean.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        try:
            writer = csv.writer(csvfile)
            writer.writerow([ingredient_names_clean,number,unit])
        except NameError as e:
            print(e)
        except JSONDecodeError as e:
            print(e)

def fraction_to_float(s):
    list_str=list(s.group())
    n=round(int(list_str[0])/int(list_str[2]),3)
    return str(n)+",".join(list_str[3:]).replace(",","")

def clean_food(ingredient_names):
    a = ingredient_names.replace("半", "0.5").replace("１", "1").replace("０", "1").replace("２", "2") \
        .replace("３", "3").replace("４", "4").replace("５", "5").replace("（", "(").replace("）", ")")
    b = re.split(r"\d", a)[0]
    c = re.sub(r"([^\u4e00-\u9fa5\u0041-\u005A\u0061-\u007A]|一(包|碗|小碗|附)|(適|少)(量|當|許)|新鮮|市售|\
    |隔夜|切(段|絲|成|塊|片|碎末|花|碎|小丁|丁|末|細|條|小(塊|段))|約|(或|可(不用|用|依|選|均勻|不加|視家裡|\
    |替換|省略|切分|以)).*)|(皆|亦|即|也|均)可|(此次|一(個|支|大匙|小(撮|匙)|隻|把)|(依|視)個人|又(稱|名)).*|\
    |兩(?!節|層).*|數.*|少|個人包|成分|手切|去(皮|骨)|帶皮|現炒|原味|吃剩的|一(?!即|般)|小$.*|斜段|大碗|\
    |份量|沾醬|方便製作的|宜口為主|建議|表面裝飾", "", b)
    d = re.sub(r"各$|各(式|種)|片狀|特級冷壓初榨|剝殼|方便製作的份量|不同|小(丁|束)|酌量|茄子重量的|沒餡|付煮熟|\
    |幾滴|裝飾用|煮切|去殼|醃料分成|鍋子.*", "", c)
    ingredient_names = re.sub("飯{2}", "飯", d)
    return ingredient_names

def clean_unit(ingredient_units):
    # 要有順序性的取代，否則有反效果，一開始就用RE模組可能誤抓
    ingredient_units = re.sub(r"半\b", "", ingredient_units).replace("1小半", "0.5").replace("小半", "0.5") \
        .replace("一半", "0.5").replace("半", "0.5").replace("1½", "1.5").replace("½", "0.5").replace("⅓", "0.333") \
        .replace("數", "x").replace("／","/").replace("～","~")\
        .replace("一般", "").replace("一", "1").replace("１", "1").replace("０", "1").replace("２", "2") \
        .replace("３", "3").replace("４", "4").replace("５", "5").replace("（", "(").replace("）", ")")
    # 找全形數字
    k = re.search(r"[\uFF10-\uFF19]", ingredient_units)
    if k:
        print(k.group())
    else:
        pass
    # 怕這些形容詞在真正的單位詞前面
    list_ingredient_units = ["適量", "酌量", "少量", "幾片", "幾滴", "少許", "些許"]
    for n, j in enumerate(list_ingredient_units):
        ingredient_units = ingredient_units.replace(str(j),"5g")
    try:
        ingredient_units = re.search(r"(([0-9]|x).*)", ingredient_units)
        ingredient_units = ingredient_units.group()
        ingredient_units = re.sub(r"(\({1}\D*\))", "", ingredient_units)
        ingredient_units = re.sub(r"\(百分比.*", "", ingredient_units)
        ingredient_units = re.sub(r"c+\.c+\.?", "cc", ingredient_units)
        ingredient_units = ingredient_units.replace("，依個人喜好調整", "").replace("約", "").replace(",", "")
        ingredient_units = re.sub(r"\s", "", ingredient_units)

        ingredient_units = re.sub(r"的量*", "", ingredient_units)
        #轉換數量從分數變成小數 1/2=>0.5
        ingredient_units = re.sub(r"\d(\／|\/)\d.*", fraction_to_float, ingredient_units)
        x = re.search(r"\d*(k)?(g|公克|克)", ingredient_units)
        if x:
            # 有KG被抓進來
            ingredient_units = x.group()
            return ingredient_units
        else:
            y= re.search(r"(\~|\∼).*", ingredient_units)
            if y:
                ingredient_units = y.group()
                ingredient_units=ingredient_units.replace("~","").replace("∼","")
                return ingredient_units
            else:
                return ingredient_units
    except NameError as e:
        print(e)
    except AttributeError as e:
        print(e)



def main():
    #讀所有json
    json_list=os.listdir(path)
    for i in json_list:
        try:
            with open(path + "/" + i, "r", encoding="utf-8") as f:
                try:
                    dic = f.read()
                    d = json.loads(dic)
                    list_ingredients = d["ingredients"]
                    for i in list_ingredients:
                        #清理食材
                        ingredient_names = i["ingredient_names"]
                        ingredient_names_clean=clean_food(ingredient_names)

                        #清理數量與單位
                        ingredient_units=i["ingredient_units"]
                        ingredient_units_clean=clean_unit(ingredient_units)

                        #分隔數量與單位
                        number=split_ingredient_units_to_number(ingredient_units_clean)
                        unit=split_ingredient_units_to_unit(ingredient_units_clean)
                        #輸出CSV
                        #csv_to_out(ingredient_names_clean,number,unit)

                        print(ingredient_units_clean,"        ","   ",unit)
                except ValueError as e:
                    print(e)
                except JSONDecodeError as e:
                    print(e)
        except PermissionError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
if __name__ == "__main__":
    main()




