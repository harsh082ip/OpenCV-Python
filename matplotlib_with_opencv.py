import cv2
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt;

img = cv2.imread('data from opencv/lena.jpg', 0)
cv2.imshow('img', img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img, cmap='gray')
plt.show()

cv2.waitKey(1)
cv2.destroyAllWindows()