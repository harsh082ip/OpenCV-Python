import cv2
print(cv2.__version__)


# Readinng an image locally and saving in form of indexes
img = cv2.imread('data from opencv/home.jpg', 1)
print(img)

# Displaying an image using a waitkey of 6000 miliseconds
cv2.imshow('image', img)
k = cv2.waitKey(0)
# used to destroy all the windows
cv2.destroyAllWindows()

# writing an image
cv2.imwrite('home_copy.jpg', img)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('homw_copy2.jpg', img)
    cv2.destroyAllWindows()