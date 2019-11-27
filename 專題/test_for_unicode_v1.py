import pandas as pd
import os,json,re,sys

#print("{:#X}".format(16))

def trans(s,unicode_down,unicode_up):
    #依序將unicode_down跟unicode_up範圍內的每一個字先轉成十進位算範圍，再轉回utf-8做sub取代
    D={}
    for full_str in range(int("0x"+unicode_down,16),int("0x"+unicode_up,16)+1):
        half_str=full_str-65248
        a=str(hex(full_str).split("x")[1])
        a="\\u"+"{:0>4s}".format(a)
        b=str(hex(half_str).split("x")[1])
        b ="\\u"+"{:0>4s}".format(b)
        D[a]=b
    print(D)
        #print(a)
    if re.search(r"[\uFF10-\uFF19]",s):
        k=re.search(r"[\uFF10-\uFF19]", s)
        print(k.group())
        #for i in list(s):

            # #將大寫數字轉成小寫數字，ord()可將字串轉成utf-8十進制整数 chr()則是反函數,觀察全形和半形差65248變可轉換 半形數字0-9


trans("１123321","FF10","FF19")

#print(re.sub("uff11","1","１"))