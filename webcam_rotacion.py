# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:57:19 2019

@author: alx34
"""

import numpy as np
import cv2
from scipy import ndimage

cap = cv2.VideoCapture()
cap.set(3, 640)
cap.set(4, 480)
ret, frame = cap.read()

x = 0
d = 0
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img_out = ndimage.rotate(frame, d, reshape=False)

    if d <= 45 and x == 0:
        d = d + 3
        if d >= 45:
            x = 1
    elif d >= -45 and x == 1:
        d = d - 3
        if d <= -45:
            x = 0

    cv2.imshow('frame', frame)
    cv2.imshow('frame_eq', img_out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
