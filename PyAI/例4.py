import cv2 as cv
import numpy as np
def extrace_hair(image): #抓頭髮顏色 P62
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("HSV11", hsv)
    low_hsv=np.array([0,0,0])
    high_hsv=np.array([180,255,46])
    dst=cv.inRange(hsv,low_hsv,high_hsv) #對圖每個點做 鎖定
    cv.imshow("result",dst)
def extrace_object_demo():  #抓carma的綠色
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        dst = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("Video", frame)
        cv.imshow("mask", dst)
        cv.imshow("hsv", hsv)
        c = cv.waitKey(50)  #0.05秒偵測一次
        if c == 27: #esc鍵
            break
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src=cv.imread("F:/photo/b.jpg")
cv.namedWindow("input image",cv.WINDOW_NORMAL)#不寫 預設是AUTO_SIZE
#cv.imshow("input image",src)


#extrace_hair(src)
#extrace_object_demo()
#三通道的分離 .split
b,g,r=cv.split(src)
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# #三通道合併
src1=cv.merge([b,g,r])
cv.imshow("src1",src1)

#extrace_object_demo()
cv.waitKey(0)
cv.destroyALLWindows()