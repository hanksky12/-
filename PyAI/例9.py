import cv2 as cv
import numpy as np

#########再加一個原圖做高斯
def clamp(pv):  #限制元素 定回0-255之內
    if pv > 255:
        return 255
    if pv < 0:
        return  0
    else:
        return  pv
'''
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
'''
#做出高斯噪聲  (實際運用:可藏資訊  用特定的噪聲去加碼  收到的人要用特定方法解碼
def gaussian_noise(image):                   #加入燥聲
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            #帶有高斯函數的圖像 # normal ==>最高不大於1   0是高斯函數的中心點  20是高斯函數的標準差=胖瘦(值越小越瘦高) 製造符合高斯函數的值給我三份
            s = np.random.normal(0,20,3)
            b = image[row, col, 0]           #blue那一面矩陣
            g = image[row, col, 1]           #green那一面矩陣
            r = image[row, col, 2]           #red那一面矩陣
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image",image)
    aaa = cv.GaussianBlur(image, (5,5), 0)
    cv.imshow("re noise image", aaa)



print("----------- Hello Python ------------")
src = cv.imread("F:/photo/a.jpg")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片

t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("time consume : %s"%(time*1000))
##########高斯模糊
dst = cv.GaussianBlur(src,(5,5),0)  #奇數  高斯核=卷稽核=mask=5*5
cv.imshow("Gaussian Blur",dst)                       # 秀出高斯模型
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗


