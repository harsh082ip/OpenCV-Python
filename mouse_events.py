import cv2
import numpy as np

# dir() is an inbuilt method which will show all class and methods inside cv2 package
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_ITALIC
        strCoord = str(x) + ', ' + str(y)
        cv2.putText(img, strCoord, (x,y), font, 1, (225, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue)+ ',' + str(green) + ','+ str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (225, 44, 0), 2)
        cv2.imshow('image', img)


img = cv2.imread('data from opencv/lena.jpg', 1)

cv2.imshow('image', img)
cv2.setMouseCallback('image', clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.setMouseCallback('Image', clickEvent)
