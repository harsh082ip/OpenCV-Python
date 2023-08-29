import cv2


cap = cv2.VideoCapture(0)

print(cap.isOpened())
# isOpended() will give true or false if it starts capturing the video
while(cap.isOpened()):

    # ret will store true or false depending upon the status of frame
    # and frmae will store the video frame
    ret, frame = cap.read()

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # converting the frames to grey
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # for displaying the frame
    cv2.imshow('video', grey)

    # we will give 1 ms time so that video frame will not drop and 0xFF frame is required in some systems of 64 bits
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()