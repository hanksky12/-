import cv2 as cv
import numpy as np
def fill_color_demo(image):
    copyImg = image.copy()     #複製影像至 copyImg
    h, w = image.shape[:2] #取 0,1==>高,寬    不取通道
    mask = np.zeros([h+2,w+2],np.uint8)  #0我才做處理        #記住：遮罩mask 要在img的h w 之上加2，基于opencv定義描算法
    (b,g,r) =copyImg[158, 53]      #用小畫家找種子點 小畫家是長x寬==>行x列(53,158)!!!!!!要轉成列X行(158,53) !!!!!!!!!!!!!!!!!!!!!!!
    print("位置(x=105,y=172)處的像素 - 红:%d,绿:%d,蓝:%d" %(r,g,b))      #顯示此點像素值
    # floodFill(image, mask, seedPoint, newVal, flags=None)
    # 原圖、mask、種子點、填充颜色(0,255,255)->黃、延伸填充區域:向下範圍(30,30,30) 向上範圍(40,40,40)、參數
    # FLOODFILL_FIXED_RANGE:以原像素的RGB數值做點
    # FLOODFILL_MASK_ONLY:只抓0的部分
    cv.floodFill(copyImg,mask,(158,53),(0,255,255),(30,30,30),(40,40,40),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)
def fill_binary():
    image = np.zeros([400,400,3],np.uint8)           #創造一張 400x400 內容為零的影像
    image[100:300,100:300, : ] = 255                 #像素點高寬 100-300 內容填成 255白
    cv.imshow("fill_binary", image)

    mask = np.ones([402,402,1], np.uint8) #402*402 單通道 8BIT
    #mask[101:301,101:301] = 0
    mask[120:280, 120:280] = 0  #整張mask 中間是0 其他是1  下面把整張蓋到原圖400*400 上面 用參數FLOODFILL_MASK_ONLY只讓有0的部分發揮作用 其他1不作用
    cv.floodFill(image, mask, (200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY) #(200,200)是沒用的點可以是mask任意點，但是要參數不能少  (0,0,255)->紅色
    cv.imshow("filled_binary", image)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src=cv.imread("F:/photo/3002.jpg")
cv.namedWindow("input image",cv.WINDOW_NORMAL)#不寫 預設是AUTO_SIZE
cv.imshow("input image",src)

fill_color_demo(src)
#fill_binary()
cv.waitKey(0)
cv.destroyALLWindows()