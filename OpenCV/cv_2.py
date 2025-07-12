# Morphological operation
import cv2
import numpy as np


img1 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg",0)
img2 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg")

width = 600
height = 850
dim = (width, height)

Resized = cv2.resize(img2, dim)

kernel = np.ones((5, 5), np.uint8)

# Erosion
# Erosion = cv2.erode(Resized, kernel, iterations=1)

# Dilation
# Dilation = cv2.dilate(Resized, kernel, iterations=1)

# Opening
# Opening = cv2.morphologyEx(Resized, cv2.MORPH_OPEN, kernel)

# Closing
# Closing = cv2.morphologyEx(Opening, cv2.MORPH_CLOSE, kernel)

# Gradient
# Gradient = cv2.morphologyEx(Resized, cv2.MORPH_GRADIENT, kernel)

# Tophat
Tophat = cv2.morphologyEx(Resized, cv2.MORPH_TOPHAT, kernel)

# Blackhat
Blackhat = cv2.morphologyEx(Resized, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", Resized)
# cv2.imshow("Erosion", Erosion)
# cv2.imshow("Dilation", Dilation)
# cv2.imshow("Opening", Opening)
# cv2.imshow("Closing", Closing)
# cv2.imshow("Gradient", Gradient)
cv2.imshow("Tophat", Tophat)
cv2.imshow("Blackhat", Blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()