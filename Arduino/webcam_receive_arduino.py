import cv2
import serial
import time

# Set the correct serial port and baud rate (9600 is the default in this case)
SERIAL_PORT = 'COM3'  # Change this to your actual serial port (e.g., /dev/ttyACM0 or /dev/ttyUSB0 on Linux)
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.01)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
led_status = False
while True:
    ret_val, frame = cam.read()
    line = ser.readline().decode('utf-8').strip()
    if line == "LED ON":
        print("LED is ON")
        led_status = True
    elif line == "LED OFF":
        print("LED is OFF")
        led_status = False

    # If the LED is ON, overlay "LED ON" on the video
    if led_status is True:
        cv2.putText(frame, "LED ON", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif led_status is False:
        cv2.putText(frame, "LED OFF", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the resulting frame with overlay text
    cv2.imshow('Webcam Feed', frame)

    # Check if the user presses 'q' to quit
    if cv2.waitKey(1) == 27:
        break  # esc to quit

cv2.destroyAllWindows()
