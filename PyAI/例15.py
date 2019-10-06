import cv2 as cv
import numpy as np

############模板匹配
#在模板中取定任A點，對於A點其他點與A點的色彩距離做紀錄成矩陣  M(m,n)或 M(m*n,1)
#在原圖上以卷積方法,用矩陣大小m*n算出距離記錄下來,並將每次得到的矩陣與M相減計算成value    value數=(原圖列數-小圖列數+1)*(原圖行數-小圖行數+1))畫圖可懂
def template_demo():
    tpl = cv.imread("E:/photo/g.png")
    target = cv.imread("E:/photo/f.png")
    cv.imshow("template image",tpl)
    cv.imshow("target image", target)
    #0:TM_SQDIFF 1:TM_SQDIFF_NORMED 2:TM_CCORR 3:TM_CCORR_NORMED 4:TM_CCOEFF 5:TM_CCOEFF_NORMED
    #methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]#三種演算法代碼     全部1-6
    methods = [cv.TM_SQDIFF, cv.TM_CCORR, cv.TM_CCOEFF]
    print(methods)
    th, tw = tpl.shape[:2]       #tpl該圖   th:列數  tw:行數
    for md in methods:##對三種方法
        result = cv.matchTemplate(target,tpl,md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)  #將最小值 最大值 最小值位置 最大值位置放進變數
        if md == cv.TM_SQDIFF_NORMED:###這個方法要找最小
            tl = min_loc
        else:###其他兩個方法找最大
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th);
        cv.rectangle(target,tl,br,(0,0,255),2)##原圖所用的長方形 左上角座標  右下角座標 線的顏色(紅) 線的寬度
        cv.imshow("match-" + np.str(md),target) #秀出紅框
        #cv.imshow("match-(result)" + np.str(md),result) #秀出比對結果
print("----------- Hello Python ------------")
src = cv.imread("E:/photo/f.png")              # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
template_demo()
cv.waitKey(0)                                        # 等待使用者按按鍵
cv.destroyWindow("Input Image")                      # 關閉視窗




