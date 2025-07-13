import cv2

img = cv2.imread('images/highway.jpg')

Resize = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

ksize = (7, 7)

SigmaX = 0
SigmaY = 0

Blur = cv2.GaussianBlur(Resize,ksize,0)


cv2.imshow('Resize',Resize)
cv2.imshow('Blur',Blur)



cv2.waitKey(0)
cv2.destroyAllWindows()
