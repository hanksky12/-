import cv2 as cv
import numpy as np
#以下都用卷積
#########均值模糊化:有雜訊(噪聲)   以平均值取代
def blur_demo(image):
    det = cv.blur(image,(5,5))   # mask=5*5大小
    cv.imshow("blur",det)

#########中值模糊:有雜訊(噪聲)     以中位數取代 作法:先做排序後，因為與其他點特別不一樣，所以該點會在最後或最後，再以中位數取代
def median_blur_demo(image):
    det = cv.medianBlur(image,5) #必須是奇數  只需打一個number
    cv.imshow("blur", det)

#########銳化處理:讓邊緣更突出    以mask:矩陣正中間數用大倍數，其他用1倍，對想要邊緣的地方跑mask(kernel)
def custon_blur_demo(image):                                                  #自訂義卷積
    #kernel = np.ones([5,5],np.float32)/25                                    #自訂義的 filter  一維
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0,-1, 0]], np.float32)       # 自訂義的 filter 二維 (銳化)
    det = cv.filter2D(image,-1,kernel = kernel) #這個函數會自動去找圖片內邊緣做運算  參數-1 新影像跟原本channl數一樣
    cv.imshow("custon_blur_demo", det)


print("----------- Hello Python ------------")
src = cv.imread("F:/photo/a.jpg")               # 讀取圖檔
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小
cv.imshow("Input Image",src)                         # 顯示圖片
blur_demo(src)
#median_blur_demo(src)##這邊用c.jpg
#custon_blur_demo(src)
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗

