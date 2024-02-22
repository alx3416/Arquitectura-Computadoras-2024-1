import cv2
import numpy as np

kernel = np.array([-1, 1])
cam = cv2.VideoCapture(1)
while True:
    ret_val, img = cam.read()

    # create local function
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols, channels = img.shape
    img_out = img_gray.copy()

    cv2.imshow('my webcam', img_out)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
cv2.destroyAllWindows()
