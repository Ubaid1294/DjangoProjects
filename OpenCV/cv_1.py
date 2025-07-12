import cv2

img1 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg",0)
img2 = cv2.imread("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/highway.jpg")

print("Dimensions of an Image: ", img1.shape)
print("Dimensions of an Image: ", img2.shape)

width = 400
height = 400
dim = (width, height)

resized = cv2.resize(img1, dim)

cv2.imshow("window", resized)


# cv2.imwrite("C:/Users/AABID HUSSAIN/PycharmProjects/gitclone/OpenCV/images/Car.jpg", img)

cv2.waitKey(0)

cv2.destroyAllWindows()