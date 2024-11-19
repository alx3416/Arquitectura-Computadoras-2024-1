import numpy as np
import cv2
import os


# Set your camera
capL = cv2.VideoCapture(1, cv2.CAP_DSHOW)
capR = cv2.VideoCapture(2, cv2.CAP_DSHOW)

# Set these for high resolution
#capL.set(3, 1920)  # width
#capL.set(4, 1080)  # height
#capR.set(3, 320)  # width
#capR.set(4, 240)  # height

output_folderL = 'calibrationL'
output_folderR = 'calibrationR'

# Create the folder if it doesn't exist
if not os.path.exists(output_folderL):
    os.makedirs(output_folderL)
if not os.path.exists(output_folderR):
    os.makedirs(output_folderR)

i=0
while True:
    # Capture frame-by-frame
    ret, frameL = capL.read()
    ret, frameR = capR.read()

    # Display the resulting frame
    cv2.imshow('frameL', frameL)
    cv2.imshow('frameR', frameR)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        cv2.imwrite(output_folderL + "/" + "L" + str(i) + ".png", frameL)
        cv2.imwrite(output_folderR + "/" + "R" + str(i) + ".png", frameR)
        i += 1

# When everything done, release the capture
capL.release()
cv2.destroyAllWindows()
capL.release()
