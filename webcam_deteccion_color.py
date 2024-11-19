import numpy as np
import cv2
from deteccion_color import deteccion_color

# from <archivo.py> import <mifuncion> # Ejemplo para importar una función en archivo py

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
ret, frame = cap.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    Im2 = deteccion_color(frame)

    # Display the resulting frame
    cv2.imshow('Procesado', Im2)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
