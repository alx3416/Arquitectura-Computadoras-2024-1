# Para usar funciones en otro programa, hay que agregar definición al inicio
# from <archivo.py> import <mifuncion> # Ejemplo para importar una función en archivo py

def deteccion_color(img_in):  # Nombre de la función y variables de entrada
    # Librerias a usar en esta función
    import numpy as np
    import cv2

    img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2LAB)

    L = img_in[:, :, 0]
    a = img_in[:, :, 1]  # Tomamos canal a (verdes negativo (0-127) y rojos positivo (128-25))
    b = img_in[:, :, 2]  # tomamos canal b (positivos amarillo, negativos azules)
    # L = np.double(L) # Conversión tipo de dato
    a = np.double(a)
    b = np.double(b)
    a = a - 128
    b = b - 128

    # z=(np.bitwise_and(a>0,a>np.abs(b))) # Detección de rojos
    # z=np.bitwise_and(a<0,np.abs(a)>np.abs(b)) # Detección de verdes
    z=np.bitwise_and( b>0, b>np.abs(a) ) # Detección de amarillos
    # z = np.bitwise_and(b < 0, np.abs(b) > np.abs(a))  # Detección de azules

    new_a = a
    new_b = b
    new_a[z == 1] = b[z == 1]
    new_b[z == 1] = a[z == 1] * (-1)

    img_in[:, :, 0] = L
    img_in[:, :, 1] = new_a + 128
    img_in[:, :, 2] = new_b + 128

    img_out = np.uint8(img_in)
    img_out = cv2.cvtColor(img_out, cv2.COLOR_LAB2BGR)

    # variables de salida
    return img_out
