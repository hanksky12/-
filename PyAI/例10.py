import cv2 as cv
import numpy as np
###############邊緣保留濾波 之前的模糊由於是對整張圖模糊化導致邊緣也不清楚
"""
    高斯雙邊模糊:
    d：即 distance，常規爲 0 ，像素的鄰域直徑，可有sigmaColor和sigmaSpace計算可得；
    sigmaColor：儘量取大，目的將小的差異模糊掉，噪聲去掉
    sigmaSpace：儘量取小，那麼“核”就小一點，主要的差異就保留下來
"""
#第一種方法

def bi_demo(image):                                  #定義雙邊濾波函數
    dst = cv.bilateralFilter(image,0, 100, 15)   #0==>半徑 100顏色的標準差  15空間的標準差
    cv.imshow("bi_demo",dst)

#第二種方法
def mean_shift_demo(image):                          # 定義均值偏移濾波
    dst = cv.pyrMeanShiftFiltering(image, 10, 50) #空間半徑 #色彩半徑
    cv.imshow("mean_shift_demo", dst)


print("----------- Hello Python ------------")
src = cv.imread("F:/photo/a.jpg")         # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)
bi_demo(src)
mean_shift_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗


