# Channel --> 0 - 255
import cv2
import numpy as np

img = cv2.imread('images/highway.jpg',0)

threshold_Val = 100

_ ,Binary_threshold =  cv2.threshold(img,threshold_Val,255,cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.imshow("Binary Threshold",Binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()