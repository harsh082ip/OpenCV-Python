import cv2
import numpy as np

img = cv2.imread('data from opencv/home.jpg', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
# till the thresh the value of pixel will not change, after then it will remain as thresh
_, th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
# when pixel value is lesser than thresh, the pixel assign is 0, and when it is greater than
# 50(thresh), it will remain same
_, th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
# it is a vice versa of above
_, th5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('img', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()