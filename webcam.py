import cv2
import numpy as np

kernel = np.array([-1, 1])
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    ret_val, img = cam.read()

    # create local function
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols, channels = img.shape
    img_out = img_gray.copy()
    kernel1 = np.array([[0.111, 0.111, 0.111],
                        [0.111, 0.111, 0.111],
                        [0.111, 0.111, 0.111]])

    img_out = cv2.filter2D(src=img_gray, ddepth=-1, kernel=kernel1)
    img_out = (img_out+255)/512

    cv2.imshow('my webcam', img_out)
    cv2.imshow('original', img)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
cv2.destroyAllWindows()
