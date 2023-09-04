import cv2
import numpy as np

img = cv2.imread('data from opencv/messi5.jpg')
img2 = cv2.imread('data from opencv/opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img2)
img = cv2.merge((b, g, r))

# ball = img[280:340, 330:390]:
#
# This line extracts a region of interest (ROI) from the img image.
# The ROI is defined by a specific rectangular area specified by coordinates.
# The format is img[y1:y2, x1:x2], where (y1, x1) represents the top-left corner and (y2, x2) represents the bottom-right corner of the rectangular region.
# In this case, img[280:340, 330:390] selects a rectangular region from (280, 330) to (339, 389) in the img image. This rectangular region is essentially a portion of the image, and it is assigned to the variable ball.
# img[273:333, 100:160] = ball:
#
# This line replaces another rectangular region in the img image with the content stored in the ball variable.
# Similar to the previous line, it defines a rectangular region with coordinates (273, 100) as the top-left corner and (332, 159) as the bottom-right corner.
# The content of the ball variable (the region previously extracted from the image) is then assigned to this rectangular region in img.

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# # img = cv2.resize(img, (512, 512))
# img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()