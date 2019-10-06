import cv2 as cv
import numpy as np

def video_demo():
    capture=cv.VideoCapture(0)
    while(True):
        ret, frame= capture.read()#ret代表有沒有讀到 video True or False    frame 存放影像的變數
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50) #50毫秒讀一次
        if c==27: #ESC的 ASC碼代號
            break

def get_image_info(image):
    print(type(image))#資料型態
    print(image.shape)#高,寬,通道    rows,columns,matrixs
    print(image.size)#上面相乘 =pixel   elements
    print(image.dtype)#pixel type
    pixel_data=np.array(image)    #用array去讀
    print(pixel_data)
    #print(classimage.shape)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


src=cv.imread("F:/photo/a.jpg")   #路徑不吃中文 和WINDOW路徑\要改 /
cv.namedWindow("input image",cv.WINDOW_NORMAL)#不寫 預設是AUTO_SIZE
cv.imshow("input image",src)

#video_demo()
get_image_info(src)
# gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY) #彩色轉灰階 用內建函式都有優化過速度快 不要手寫
# cv.imwrite("E:\image\gray001.jpg",gray) #灰階做存檔
cv.waitKey(0) #等待指令一定要不然   imshow執行後立刻關掉
cv.destroyWindow("input image")





