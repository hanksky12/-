import cv2 as cv
import numpy as np
def create_rgb_hist(image):                          # 創建 rgb 直方圖
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)  #做一個多列*1行   當直方圖使用 預設0次  之後迴圈每算出一個值放到對應位置+1
    bsize = 256 / 16                             # 256色/(每16色當一組)=  16組
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            # 將bgr都以每16色分組，r的第幾組放在16*2位+g的第幾組放在16*1位+r的第幾組放在16*0位(EX:十位數123=1x10*2+2x10*1+3x10*0)
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize) #np.int取最接近該數的最小整數
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1    #做直方圖的累計 每算出一個值就在該直方位置+1 跑完整張圖 直方圖的累計完成
    return rgbHist
def hist_compare(image1,image2):                      # 直方圖比較
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    #比較直方圖
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)    #巴氏距離比較，越小越相似
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)           #相關性比較（最大為1）：越接近1越相似
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)           #卡方比較，越小越相似
    print("巴氏：%s   相關性：%s   卡方：%s"%(match1,match2,match3))


print("----------- Hello Python ------------")
src1 = cv.imread("F:/photo/a.jpg")              # 讀取圖檔
src2 = cv.imread("F:/photo/a.jpg")              # 讀取圖檔
cv.imshow("Input Image",src1)                        # 顯示圖片
cv.namedWindow("Input Image",cv.WINDOW_AUTOSIZE)     # 自動調整視窗大小

hist_compare(src1,src2)                              # 這裡可以讀兩張一樣的圖比較
cv.waitKey(0)                                        # 等待使用者按按鍵

cv.destroyWindow("Input Image")                      # 關閉視窗



