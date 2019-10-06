import cv2 as cv
import numpy as np

def color_sapce_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray11",gray)  #這邊創造的gray11是一個檔案名稱,後面名稱不能一樣不然只會呈現一個
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("HSV11", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("YUV11", yuv)
    YCrCb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("YCrCb11", YCrCb)



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src=cv.imread("F:/photo/a.jpg")
cv.namedWindow("input image",cv.WINDOW_NORMAL)#不寫 預設是AUTO_SIZE
cv.imshow("input image",src)

color_sapce_demo(src)



cv.waitKey(0)
cv.destroyALLWindows()