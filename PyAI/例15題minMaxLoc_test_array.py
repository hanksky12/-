import numpy as np
import cv2
a=np.array([[1,2,3,4],[5,8,67,9]])
min_val,max_val,min_indx,max_indx=cv2.minMaxLoc(a)

print(min_val,max_val,min_indx,max_indx)
