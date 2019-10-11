import cv2 as cv
import numpy as np


def threshold_demo(image):    #全域值
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #轉灰階
    ##cv.THRESH_OTSU(適合雙峰) 和 cv.THRESH_TRIANGLE(適合單峰)幫助我們自動選閥值(前面如果有自訂閥值就無效)  可手動選  前面自訂  後面就不要寫這兩個函數
    # output 前面是的閥值 後面是影像
    #ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)    #自動選閥值+THRESH_BINARY方法
    #ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO) ##閥值自選 + THRESH_TOZERO方法
    print("threshold value %s"%ret)
    cv.imshow("binary",binary)
def local_threshold(image):   #區域值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25, 10)
    cv.imshow("binary",binary)

print("----------- Hello Python ------------")
src = cv.imread("E:/photo/a.jpg")              # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
threshold_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗
