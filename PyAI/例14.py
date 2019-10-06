import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#######2D直方圖   x軸:放H    Y軸:放S   累計次數:亮度表示
def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    hist = cv.calcHist([image],[0,1], None,[180,256],[0,180,0,256])  #計算 HS [0,1]兩通道 想在直方圖呈現的Y軸0-180 X軸0-256
    # OpenCV中 H 的取值範圍為0 ~180 (8bit儲存時)
    plt.imshow(hist,interpolation='nearest')     # 用最接近數值的方式統計,因為RGB轉HSV會有小數點 無法歸類
    plt.title("2D Histogram")
    plt.show()

###反向投影應用  用sample裡的目標顏色  到 target裡去抓出顏色(越白表示越符合)
#平常藉由圖來算直方圖  這個是藉由直方圖來搭配目標來抓出顏色
def back_projection_demo():
    sample = cv.imread("F:/photo/h.jpg")
    target = cv.imread("F:/photo/a.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show image
    #cv.imshow("sample",sample)
    #cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[36,48],[0,180,0,256]) #180-->36bin(每5個合併),256--->48bin(每5.33個合併)  顏色容忍度變大(不要算得那麼細)==>對比到的目標位置變多了  ,hsv只用 HS [0,1]兩通道
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)                  #計算出來的值規一化到 0-255 之间 透過某種距離將每個值值重新賦予另一個範圍，值與值之間距離比例不變 看文件
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)   #在較大的途中找特定的圖像 目標的圖要記得[]  模板的圖 直方圖反向投影 #1==>1倍
    cv.imshow("back_projection_demo",dst)





print("----------- Hello Python ------------")
src = cv.imread("F:/photo/a.jpg")              # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
#hist2d_demo(src)
back_projection_demo()
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗



