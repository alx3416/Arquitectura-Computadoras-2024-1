import cv2
import numpy as np

kernel = np.array([-1, 1])
cam = cv2.VideoCapture(0)
while True:
    ret_val, img = cam.read()

    # create local function
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols, channels = img.shape
    img_out = img_gray.copy()
    for row in range(rows-1):
        for col in range(cols):
            img_out[row][col] = float(img_gray[row][col]) - float(img_gray[row + 1][col])
            img_out[row][col] =np.uint8((img_out[row][col] + 255)/2)

    cv2.imshow('my webcam', img_out)
    cv2.imshow('original', img)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
cv2.destroyAllWindows()
