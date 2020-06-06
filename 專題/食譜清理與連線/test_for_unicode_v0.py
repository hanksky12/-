
import pandas as pd
import os,json,re,sys
#print(int("0xFF10",16))
# a="１".encode(encoding='utf-8')
# a=hex(a)
# a=int(a,16)
#a=a.decode(encoding="unicode_escape")
# print(type(a))

print(sys.getdefaultencoding())
# def trans(s):
#     #先轉utf-8的10進制，觀察全形和半形差65248變可轉換，最後-48是因為可得到數字
#     if ord(s)>=65296 and ord(s)<=65305:
#         # 半形數字0-9
#         n=ord(s)-65248-48
#         return n
# print(trans("１"))
#
# # for i in ["１","2","3"]:
# #     s=trans(s)
# #     if s in range(30,40):
# #         print(s)
# k=re.search(r"[\uFF10-\uFF19]","砂糖51g１")
# print(k.group())

    # k = re.sub(r"[\uFF10-\uFF19]", r"[\u0030-\u0039]", i)
    # print(k)
#print(int("0x"+"FF10",16))


def trans(str,unicode_down,unicode_up):
    for i in range(int("0x"+unicode_down,16),int("0x"+unicode_down,16)):
        if i == ord(str):
            print(i)
            #將大寫數字轉成小寫數字，ord()可將字串轉成utf-8十進制整数 chr()則是反函數,觀察全形和半形差65248變可轉換 半形數字0-9
            #s = chr(ord(str) - 65248)

        else:
            print("123")

trans("１","FF10","FF19")

#print(int("0x"+"FF10",16))