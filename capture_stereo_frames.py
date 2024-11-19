import cv2
import os

# Define the folder to save snapshots
output_folderL = 'snapshotsL'
output_folderR = 'snapshotsR'

# Create the folder if it doesn't exist
if not os.path.exists(output_folderL):
    os.makedirs(output_folderL)
if not os.path.exists(output_folderR):
    os.makedirs(output_folderR)

# Initialize the webcam
capL = cv2.VideoCapture(0)
capR = cv2.VideoCapture(1)

if not capL.isOpened():
    print("Error: Could not open left webcam.")
    exit()
if not capR.isOpened():
    print("Error: Could not open right webcam.")
    exit()
snapshot_count = 0
while True:
    # Read a frame from the webcam
    retL, frameL = capL.read()
    retR, frameR = capR.read()

    if not retL:
        print("Error: Could not read frame.")
        break
    if not retR:
        print("Error: Could not read frame.")
        break

    # Display the frame in a window
    cv2.imshow('WebcamL', frameL)
    cv2.imshow('WebcamR', frameR)

    # Wait for user input
    key = cv2.waitKey(1) & 0xFF

    snapshot_filenameL = os.path.join(output_folderL, f'snapshot_{snapshot_count}.png')
    snapshot_filenameR = os.path.join(output_folderR, f'snapshot_{snapshot_count}.png')
    cv2.imwrite(snapshot_filenameL, frameL)
    cv2.imwrite(snapshot_filenameR, frameR)
    snapshot_count += 1
    if key == ord('q'):
        # Quit the loop
        break

# Release the webcam and close the window
capL.release()
capR.release()
cv2.destroyAllWindows()