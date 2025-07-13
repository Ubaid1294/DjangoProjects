import cv2

img = cv2.imread('images/highway.jpg')

Resize = cv2.resize(img,(520,520))

Kernal = 3

blur = cv2.medianBlur(Resize,Kernal)

cv2.imshow('Original',Resize)
cv2.imshow('Median Gaussian ',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()