import cv2


cap = cv2.VideoCapture('data from opencv/Megamind.avi')

# this is a fourcc video code
fourcc = cv2.VideoWriter.fourcc(*'XVID')
print(str(fourcc))
# aruguments ---> filename, fourcc code, frames per sec, resolution
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
# isOpended() will give true or false if it starts capturing the video
while(cap.isOpened()):

    # ret will store true or false depending upon the status of frame
    # and frmae will store the video frame
    ret, frame = cap.read()

    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # video will not be greyScaled as it it writing before conversion
        out.write(frame)
        # converting the frames to grey
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # for displaying the frame
        cv2.imshow('video', grey)

        # we will give 1 ms time so that video frame will not drop and 0xFF frame is required in some systems of 64 bits
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# .fourcc(*'XVID'): This is a method call on the VideoWriter class. It sets the codec for video compression. The fourcc stands for "four-character code," which is a code used to identify a particular video codec. In this case, 'XVID' is the codec being specified.
#
# *'XVID': This part of the code uses the * operator to unpack the characters in the string 'XVID' into separate arguments. This is because the fourcc method expects its arguments to be individual characters.
#
# 'XVID' is a commonly used codec for MPEG-4 video compression. It is often used when creating AVI video files.


