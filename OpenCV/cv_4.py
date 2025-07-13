import cv2

img1 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg",0)
img2 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg")

print("Dimensions of Original shape: ", img2.shape)

scale = 50

width = int(img2.shape[1] * scale / 100)
height = int(img2.shape[0] * scale / 100)

dim = (width, height)

Resized = cv2.resize(img2, dim, interpolation = cv2.INTER_CUBIC)

print("Dimensions of Resized shape: ", Resized.shape)
cv2.imshow("Original", img2)
cv2.imshow("Resized", Resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
