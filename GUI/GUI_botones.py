import tkinter
from tkinter import filedialog, Frame
from tkinter.constants import RIGHT

import cv2
import PIL.Image, PIL.ImageTk
import numpy as np


class App:
    def __init__(self, window, window_title, image_path="lena.jpg"):  # Agregar ruta de imagen
        self.window = window
        self.window.title(window_title)
        self.image_path = image_path
        # cargar imagen con OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        frame_left = Frame(window, borderwidth=1)
        frame_left.pack(side=tkinter.LEFT)

        # Obtener tamaño de imagen como arreglo numpy
        self.height, self.width, no_channels = self.cv_img.shape

        frame_right = Frame(window, borderwidth=1)
        frame_right.pack(side=tkinter.RIGHT)

        # Crear canvas para imagen
        self.canvas = tkinter.Canvas(frame_left, width=self.width, height=self.height)
        self.canvas.pack()

        # Uso de PIL para convertir imagen a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Añadir PIL a canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Botón para original
        self.btn_orig = tkinter.Button(frame_left, text="Original", width=30, command=self.orig_image)
        self.btn_orig.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para blur
        self.btn_blur = tkinter.Button(frame_left, text="Blur", width=30, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para bordes
        self.btn_edge = tkinter.Button(frame_left, text="Bordes", width=30, command=self.edge_image)
        self.btn_edge.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para kmeans
        self.btn_kmeans = tkinter.Button(frame_left, text="Kmeans", width=30, command=self.kmeans_image)
        self.btn_kmeans.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para kmeans
        self.btn_file = tkinter.Button(frame_left, text="Cargar imagen", width=30, command=self.file_image)
        self.btn_file.pack(anchor=tkinter.CENTER, expand=True)

        redbutton = tkinter.Button(frame_right, text="Red", fg="red")
        redbutton.pack(side=tkinter.LEFT)

        self.img_button = cv2.cvtColor(cv2.imread("blur.png"), cv2.COLOR_BGR2RGB)
        self.photo_button = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.img_button))
        greenbutton = tkinter.Button(frame_right, image=self.photo_button, fg="brown")
        greenbutton.pack(side=tkinter.TOP)

        bluebutton = tkinter.Button(frame_right, text="Blue", fg="blue")
        bluebutton.pack(side=tkinter.LEFT)

        self.window.mainloop()

    def __del__(self):
        App(tkinter.Tk(), "Tkinter y OpenCV")


    # Callback para botón "Blur"
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (7, 7))
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def edge_image(self):
        self.cv_img = cv2.Canny(self.cv_img, 75, 150)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def orig_image(self):
        self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
        dim = (self.width, self.height)
        self.cv_img = cv2.resize(self.cv_img, dim, interpolation=cv2.INTER_AREA)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def kmeans_image(self):
        img = self.cv_img
        Z = img.reshape((-1, 3))
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        self.cv_img = res.reshape(self.cv_img.shape)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def file_image(self):
        # Abre cuadro de diálogo para seleccionar imagen
        image_path = filedialog.askopenfilename()
        # verificar que path hay asea sido seleccionado
        if len(image_path) > 0:
            # imagen a grises y detectamos bordes
            self.image_path = image_path
            self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
            dim = (self.width, self.height)
            self.cv_img = cv2.resize(self.cv_img, dim, interpolation=cv2.INTER_AREA)
            self.height, self.width, no_channels = self.cv_img.shape
            #            self.canvas = tkinter.Canvas(self.window, width = self.width, height = self.height)
            #            self.canvas.pack()
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter y OpenCV")
