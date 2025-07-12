import cv2

img1 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg",0)
img2 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg")

width = 600
height = 850
dim = (width, height)

Resized = cv2.resize(img2, dim)

print("Size in bytes: ", img2.size)

cv2.imshow("Original", Resized)

print("Size in bytes: ", Resized.size)
# # Horizontal flip
# Horizontal = cv2.flip(Resized, 1)
# cv2.imshow("Horizontal flip", Horizontal)

# # Vertical flip
# Vertical = cv2.flip(Resized, 0)
# cv2.imshow("Vertical flip", Vertical)

# Vertical and Horizontal flip
Horizontal_Vertical = cv2.flip(Resized, -1)
cv2.imshow("Horizontal and Vertical flip", Horizontal_Vertical)

print("Size in bytes: ", Horizontal_Vertical.size)

cv2.waitKey(0)
cv2.destroyAllWindows()