import cv2


cap = cv2.VideoCapture(0)

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