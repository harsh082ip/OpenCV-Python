import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('data from opencv/sudoku.png', 0)
_, th1 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
# till the thresh the value of pixel will not change, after then it will remain as thresh
_, th3 = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC)
# when pixel value is lesser than thresh, the pixel assign is 0, and when it is greater than
# 50(thresh), it will remain same
_, th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
# it is a vice versa of above
_, th5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)
# print(ret)


titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

# The i+1 is used as an argument to plt.subplot(2, 3, i+1) to specify the position of the current subplot within a grid of subplots. Here's how it works:
#
# plt.subplot(2, 3, i+1) creates a subplot in a 2x3 grid, where 2 represents the number of rows, and 3 represents the number of columns.
# i+1 is used to specify the current subplot's position within this grid. Since i starts from 0, adding 1 ensures that the subplots are numbered from 1 to 6.
# This setup is commonly used when you want to arrange multiple subplots in a grid-like fashion. In your case, it's arranging 6 subplots in a 2x3 grid, where each
# subplot displays one of the images from the images list with the corresponding title from the titles list. Using i+1 ensures that each subplot is created in the correct
# position within the grid.

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


# cv2.imshow('img', img)
# cv2.imshow('th1', th1)
# # cv2.imshow('th2', th2)
# # cv2.imshow('th3', th3)
# # cv2.imshow('th4', th4)
# # cv2.imshow('th5', th5)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.show()