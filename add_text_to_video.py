import cv2
import datetime

cap = cv2.VideoCapture('data from opencv/Megamind.avi')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = "Width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + 'Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(100) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()