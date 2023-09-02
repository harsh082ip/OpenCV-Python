import cv2
import numpy as np

img = cv2.imread('white.jpg', 1)

img = cv2.line(img, (0,0), (255,255), (255, 0, 0), 8)
img = cv2.arrowedLine(img, (0,255), (255,300), (0, 255, 255), 10)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 255), 5)
img = cv2.circle(img, (255, 75), 70, (45, 255, 122), -1)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'Hello, World', (10, 500), font, 2, (168, 85, 255), 7, cv2.LINE_4)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()