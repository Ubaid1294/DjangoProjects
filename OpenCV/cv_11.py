import cv2

img  = cv2.imread('images/Bird.jpg')

resize = cv2.resize(img,(520,520))

d = 7
SigmaColor = 100
SigmaSpace = 100

b = cv2.bilateralFilter(resize,d,SigmaColor,SigmaSpace)
cv2.imshow('Input',resize)
cv2.imshow('Output',b)

cv2.waitKey(0)
cv2.destroyAllWindows()