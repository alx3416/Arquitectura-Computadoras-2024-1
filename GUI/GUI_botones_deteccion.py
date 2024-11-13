import tkinter
from tkinter import StringVar, IntVar, LEFT, RIGHT
import PIL.Image, PIL.ImageTk
import numpy as np


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Ejemplo agregar label

        self.texto = StringVar()
        self.titulo = tkinter.Label(window, textvariable=self.texto, font=("Helvetica", 16))
        self.texto.set("Detección")
        self.titulo.pack()

        # cargar imagen con OpenCV
        self.cv_img = np.zeros((512, 512, 3), np.uint8)  # Dimensiones de imagen

        # Obtener tamaño de imagen como arreglo numpy
        self.height, self.width, no_channels = self.cv_img.shape

        # Crear canvas para imagen
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Uso de PIL para convertir imagen a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Añadir PIL a canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Checks para simular entradas de datos, cambiarian estos codigos por entrada GPIO (raspberry) o Arduino (PC)
        # En caso de GPIO, se quitaria codigo de checkbutton por sensor
        # Sensor 1 - checkbutton
        self.var1 = IntVar()
        self.x1y1 = tkinter.Checkbutton(window, text="pos 1", variable=self.var1)
        self.x1y1.pack(side=LEFT, expand=False)
        # Sensor 2
        self.var2 = IntVar()
        self.x2y1 = tkinter.Checkbutton(window, text="pos 2", variable=self.var2)
        self.x2y1.pack(side=LEFT, expand=False)
        # Sensor 3
        self.var3 = IntVar()
        self.x2y1 = tkinter.Checkbutton(window, text="pos 3", variable=self.var3)
        self.x2y1.pack(side=RIGHT, expand=False)
        # Sensor 4
        self.var4 = IntVar()
        self.x2y2 = tkinter.Checkbutton(window, text="pos 4", variable=self.var4)
        self.x2y2.pack(side=RIGHT, expand=False)

        self.delay = 100  # en milisegundos, delay en caso de que sensores lo requieran
        self.update()  # función update actualiza imagen cada "delay" milisegundos
        self.window.mainloop()

    def update(self):  # Recordemos que es para camara 1, tab 2
        # toma nuevo frame de webcam
        self.cv_img = np.zeros((self.width, self.height, 3), np.uint8)
        if self.var1.get() == 1:
            self.cv_img[0:255, 0:255, 0] = 255  # cuadro rojo
        if self.var2.get() == 1:
            self.cv_img[0:255, 256:512, 2] = 255  # cuadro azul
        if self.var3.get() == 1:
            self.cv_img[256:512, 0:255, 1] = 255  # cuadro verde
        if self.var4.get() == 1:
            self.cv_img[256:512, 256:512, 0] = 255  # cuadro amarillo
            self.cv_img[256:512, 256:512, 1] = 255

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter widgets y OpenCV")
