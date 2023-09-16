import cv2
import cv2 as cv
import numpy as np

def do_nothing(x):
    print(x)

img = np.zeros((500, 750, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, do_nothing)
cv.createTrackbar('G', 'image', 230, 255, do_nothing)
cv.createTrackbar('R', 'image', 0, 255, do_nothing)
switch = '0 / 1 : on/off'
cv.createTrackbar(switch, 'image', 0, 1, do_nothing)
while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()