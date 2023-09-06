import cv2
import datetime

cap = cv2.VideoCapture('data from opencv/Megamind.avi')

while(cap.isOpened()):
    access, frame = cap.read()
    if access == True:
        font = cv2.FONT_ITALIC
        text =  str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 0, 255), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(50) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()