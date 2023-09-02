import cv2
import numpy as np

def click_Eve(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        colorImage = np.zeros((512, 512, 3), np.uint8)

        colorImage[:] = [blue, green, red]
        cv2.imshow('color', colorImage)

img = cv2.imread('data from opencv/home.jpg ', 1)
cv2.imshow('image', img)


cv2.setMouseCallback('image', click_Eve)

cv2.waitKey(0)
cv2.destroyAllWindows()