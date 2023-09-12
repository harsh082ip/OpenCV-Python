import cv2
import numpy as np

def do_nothing(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')

# In the HSV color space (Hue, Saturation, Value), the valid value ranges for each component are typically as follows:

# Hue (H):

# The hue represents the color itself and is measured in degrees.
# The usual range is 0 to 360 degrees, covering all possible colors in a color wheel.
# However, in many computer vision applications and OpenCV, the range is often scaled to 0-179 to fit within an 8-bit value. This means that the maximum value for hue in OpenCV is 179.
# Saturation (S):

# Saturation determines the purity of the color. A fully saturated color has a high intensity, while desaturated colors approach grayscale.
# The typical range is 0 to 100%, but in OpenCV and computer vision, it is usually scaled to 0-255 for an 8-bit representation. This means that the maximum value for saturation in OpenCV is 255.
# Value (V):

# Value represents the brightness or lightness of the color. A high value corresponds to a lighter color, while a low value corresponds to a darker color.
# Like saturation, the typical range for value is 0 to 100%, but it is often scaled to 0-255 in OpenCV. Therefore, the maximum value for value in OpenCV is 255.

cv2.createTrackbar('LH', 'Tracking', 0, 179, do_nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('UH', 'Tracking', 179, 179, do_nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, do_nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, do_nothing)

# 1, 79, 50, 30, 255, 255 (for orange)

while True:
    # frame = cv2.imread('data from opencv/smarties.png')
    access, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    # Define
    # lower and upper
    # bounds
    # for the HSV color range you want to track.In this case, it's blue color:
    # l_b(lowerbound) is set to[110, 50, 50], which corresponds to a bluish - greenish color.
    # u_b(upper bound) is set to[130, 255, 255], which corresponds to a slightly purplish - blue color.
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    print(type(l_b))

    # Create a mask using cv2.inRange() that filters out only the pixels within the specified HSV color range(between l_b and u_b).
    # This will create a binary image where white pixels represent the parts of the frame that match the specified color range,
    # and black pixels represent the rest.
    mask = cv2.inRange(hsv, l_b, u_b)

# In the line res = cv2.bitwise_and(frame, frame, mask=mask), the frame is indeed written twice. This might seem redundant, but it serves a specific purpose in this context.
# Let's break down what each occurrence of frame does:
# The first frame argument:
# This is the source image from which you want to extract the specific color range (blue in this case).
# It's the original color frame that you captured from the image file 'smarties.png' and loaded using cv2.imread().
# The second frame argument:
# This serves as a placeholder or a destination image where the result of the cv2.bitwise_and() operation will be stored.
# Essentially, it's a copy of the original frame, and it's used as a destination buffer for the bitwise AND operation.
# The reason for using frame as both the source and destination in this operation is to preserve the color information of the original frame while masking out the regions that don't match the specified color range. Here's how it works:
# The bitwise AND operation is performed pixel-wise between the first frame (source) and the mask. This operation retains the color information in the regions where the mask is white (i.e., where the color matches the specified range) and turns the rest black.
# The result of the operation is then stored in the second frame (destination), effectively replacing the contents of frame with the color-filtered result.
# So, using frame twice allows you to update the original frame with the filtered result, preserving the structure and size of the original image while highlighting the objects of interest based on the binary mask. It's a common practice in image processing to reuse one of the input images as the destination image when necessary.

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
