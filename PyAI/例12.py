import cv2 as cv
import numpy as np
#   equalizeHist 函數前提 :灰階1通道   因為3通道不知道對哪一通道做增強
#####全域性對比度增強  :設某值 對該值的左邊 和右邊做增強
def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #轉灰階
    dst = cv.equalizeHist(gray)     #加強函數
    cv.imshow("equalHist_demo",dst)

########局部對比增強   :設定矩陣對圖片做卷積， 每個矩陣做一次對比增強，不同矩陣不同閥值
def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))#參數第一個是對比度大小 第二個每次處理的矩陣大小
    dst = clahe.apply(gray)      # 套用矩陣各閥值儲存的陣列
    cv.imshow("clahe_demo",dst)


print("----------- Hello Python ------------")
src = cv.imread("F:/photo/a.jpg")             # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)  # 顯示圖片
#equalHist_demo(src)
clahe_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗

