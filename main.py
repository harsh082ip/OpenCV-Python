import cv2

img = cv2.imread('data from opencv/sudoku.png', 0)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)

cv2.imshow('img', img)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()