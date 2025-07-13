import cv2
from numpy.ma.core import angle

img = cv2.imread('images/highway.jpg')

row = img.shape[0]
column = img.shape[1]

center = (column/2,row/2)
angle = 300

R = cv2.getRotationMatrix2D(center,angle,1)
Rotation = cv2.warpAffine(img,R,(column,row))

cv2.imshow("Rotated Image", Rotation)
cv2.waitKey(0)
cv2.waitKey(0)