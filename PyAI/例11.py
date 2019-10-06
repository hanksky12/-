import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#三通道 合併 做直方圖
def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])   # ravel像素轉一維 把三通道的數值相加 做累計畫直方   256:幾條長方形   [0,256]直方圖的x軸要給人看得範圍0-255=>256條  [30,200]第30條到第199條               # 使用 ravel 將所有的像素資料轉為一維的陣列
    plt.show("直方圖")
# B 做一個直方圖
# G 做一個直方圖
# R 做一個直方圖
#####BGR直方圖
def image_hist(image):
    color = ('blue','green','red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])      # 計算直方圖每個 bin 的數值 參數看課本
        plt.plot(hist,color = color)                            # 劃出分布圖   指定函數 跟 曲線顏色
        plt.xlim([0,256])                                       # 设置x坐標軸範圍  可不設 預設依圖形結果
    plt.show()


print("----------- Hello Python ------------")
src = cv.imread("F:/photo/b.jpg")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)
#plot_demo(src)
image_hist(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗




