import cv2 as cv
import numpy as np

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src1=cv.imread("F:/photo/3001.png")
src2=cv.imread("F:/photo/3002.jpg")

cv.namedWindow("input image 1",cv.WINDOW_NORMAL)
cv.imshow("input image 1",src1)
cv.namedWindow("input image 2",cv.WINDOW_NORMAL)
cv.imshow("input image 2",src2)

f=src1[150:400,100:300]#對圖片取出區域
cv.imshow("f image",f)
gray = cv.cvtColor(f,cv.COLOR_BGR2GRAY)   #對該區塊 轉 彩色/3  灰階變單通
b_f=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)    #單通的值 複製 3次到三通   這一步不能跳 下一行 單通放不回三通
src1[150:400,100:300]=b_f #放回原位置
cv.imshow("b_f image",src1)

cv.waitKey(0)
cv.destroyALLWindows()