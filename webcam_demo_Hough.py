import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    cimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #    cimg = cv2.medianBlur(cimg,7)
    cimg = cv2.bilateralFilter(cimg, 11, 25, 25)
    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=80, param2=30, minRadius=30, maxRadius=70)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    #

    # Display the resulting frame
    cv2.imshow('detected circles', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
