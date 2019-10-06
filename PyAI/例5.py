import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst=cv.add(m1,m2)
    cv.imshow("add_demo",dst)
def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)
def logic_demo1(m1, m2):#and運算
    dst = cv.bitwise_and(m1, m2)
    cv.imshow("logic_demo", dst)
def logic_demo2(m1, m2): #or運算
    dst = cv.bitwise_or(m1, m2)
    cv.imshow("logic_demo", dst)
def logic_not_demo(m1):
    dst = cv.bitwise_not(m1)
    cv.imshow("logic_not_demo", dst)

def other_demo(m1, m2):
    M1,dev1 = cv.meanStdDev(m1)#平均值 標準差
    M2,dev2 = cv.meanStdDev(m2)
    h,w = m1.shape[:2]
    print(M1)
    print(M2)
    print("")
    print(dev1)
    print(dev2)
    img = np.zeros([h,w],np.uint8) #示範全黑的照片
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)
def contrast_brightness_demo(image,c,b):       #c:對比度, b:亮度
    h,w,ch = image.shape #原本影像的長 寬 通道數
    blank = np.zeros([h,w,ch],image.dtype)     #空白圖像要跟原本一樣格式一樣(大小通道都符合)
    dst = cv.addWeighted(image,c,blank,1-c,b)  #實現圖片的線性融合  前面image*c倍+後面image*1-c倍+調亮的值  PS:C可大於1，C是權重
    cv.imshow("contrast_brightness_demo",dst)



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src1=cv.imread("F:/photo/3001.png")
src2=cv.imread("F:/photo/3002.jpg")
print(src1.shape)
print(src2.shape)

cv.namedWindow("input image 1",cv.WINDOW_NORMAL)
cv.imshow("input image 1",src1)
cv.namedWindow("input image 2",cv.WINDOW_NORMAL)
cv.imshow("input image 2",src2)
#add_demo(src1,src2)     #相加看 顏色+黑0=顏色 顏色+白255=白255
#subtract_demo(src1,src2)  #相減要看誰減誰
#divide_demo(src1,src2)  #越除越小  接近0
#multiply_demo(src1,src2)  #越乘越大  接近255
#logic_demo1(src1,src2) #and 運算 黑0&顏色=黑0  白1&顏色=顏色
#logic_demo2(src1,src2) #or 運算 黑0|顏色=顏色
#logic_not_demo(src1)
other_demo(src1,src2)
#contrast_brightness_demo(src2,1.2,10)

cv.waitKey(0)
cv.destroyALLWindows()