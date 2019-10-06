import cv2 as cv
import numpy as np
def access_pixels(image):
    print(image.shape)
    print(type(image.shape))
    h=image.shape[0]
    w=image.shape[1]
    channel=image.shape[2]
    print("height:%s,width:%s,cc:%s"%(h,w,channel))
    for row in range(h):    #抓列  #對影片做反差 再存回去
        for col in range(w): #抓行
            for c in range(channel):#抓通道
                pv=image[row,col,c]#將立方體的每個 uint8 一個一個取出變成一長串
                #print((image[row,col,c]))
                image[row, col, c] =255-pv  #把做完的DATA 依原本對應位置塞回立方體
    cv.imshow("access_pixels",image)

def create_image():
    img=np.zeros([400,400,3],np.uint8)  #將每個像素設為0  自己做高400*寬400 通道3 通道大小0-255色 ,用[] 或()都可
    img[:,:,0]=np.ones([400,400])*255 #將400*400每個像素設為1再*255變全藍
    cv.imshow("create_image!!!",img)

def create_image2():
    #方法1
    # img=np.zeros([400,400,1],np.uint8)  #將每個像素設為0  自己做高400*寬400 通道3 通道大小0-255色
    # img[:,:,0]=np.ones([400,400])*127
    #方法2
    img=np.ones([400,400,1],np.uint8)
    img=img*127
    cv.imshow("create_image!!!",img)
def create_image3():
    m1=np.ones([3,3],np.float32)#每一個都是4BYTE可以是float  3*3每個element是1
    m1.fill(123.456)#這不是影像 用123.456填充
    print(m1)
    m2=m1.reshape([1,9]) #重朔矩陣
    print(m2)
def inverse(image):#等同做反差效果 而且執行速度更快
    dst=cv.bitwise_not(image)
    cv.imshow("inverse",dst)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
src=cv.imread("F:/photo/a.jpg")   #路徑不吃中文 和WINDOW路徑\要改 /
cv.namedWindow("input image",cv.WINDOW_NORMAL)#不寫 預設是AUTO_SIZE
# cv.imshow("input image",src)
#create_image()
#create_image2()
create_image3()
# inverse(src)
#
# t1=cv.getTickCount()#設定週期數 點1
# access_pixels(src)
# t2=cv.getTickCount()#設週期數  點2
# time=(t2-t1)/cv.getTickFrequency() #作時間計算  getTickFrequency:cpu頻率     週期數/(週期數/s) ===> 秒
# print("TIME:%s"%(time*1000)) #1秒=1000毫秒    這邊用毫秒表示
cv.waitKey(0)
#cv.destroyALLWindows()