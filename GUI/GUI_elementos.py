import tkinter
from tkinter import filedialog, StringVar, HORIZONTAL
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np


class App:
    def __init__(self, window, window_title, image_path="lena.jpg"):
        self.window = window
        self.window.title(window_title)

        # Ejemplo agregar label

        self.texto = StringVar()
        self.titulo = tkinter.Label(window, textvariable=self.texto, font=("Helvetica", 16))
        self.texto.set("Original")
        self.titulo.pack()

        self.image_path = image_path
        # cargar imagen con OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Obtener tamaño de imagen como arreglo numpy
        self.height, self.width, no_channels = self.cv_img.shape

        # Crear canvas para imagen
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Uso de PIL para convertir imagen a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Añadir PIL a canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Botón para original
        self.btn_orig = tkinter.Button(window, text="Original", width=30, command=self.orig_image)
        self.btn_orig.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para blur
        self.btn_blur = tkinter.Button(window, text="Blur", width=30, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        # Slider para blur (tamaño de ventana)
        self.slider1 = tkinter.Scale(window, from_=3, to=19, resolution=1, orient=HORIZONTAL)
        self.slider1.set(7)
        self.slider1.pack()

        # Botón para bordes
        self.btn_edge = tkinter.Button(window, text="Bordes", width=30, command=self.edge_image)
        self.btn_edge.pack(anchor=tkinter.CENTER, expand=True)

        # Botón para kmeans
        self.btn_kmeans = tkinter.Button(window, text="Kmeans", width=30, command=self.kmeans_image)
        self.btn_kmeans.pack(anchor=tkinter.CENTER, expand=True)

        # listado Combobox para seleccionar valores
        self.clusters = StringVar()
        self.combobox = ttk.Combobox(window, width=10, textvariable=self.clusters)
        self.combobox['values'] = (2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.clusters.set(4)
        self.combobox.pack()

        # Botón para cambiar imagen
        self.btn_file = tkinter.Button(window, text="Cargar imagen", width=30, command=self.file_image)
        self.btn_file.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback para botón "Blur"
    def blur_image(self):
        self.texto.set("Blurring")
        p = self.slider1.get()
        self.cv_img = cv2.blur(self.cv_img, (p, p))
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def edge_image(self):
        self.texto.set("Bordes")
        self.cv_img = cv2.Canny(self.cv_img, 75, 150)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def orig_image(self):
        self.texto.set("Original")
        self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
        dim = (self.width, self.height)
        self.cv_img = cv2.resize(self.cv_img, dim, interpolation=cv2.INTER_AREA)
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def kmeans_image(self):
        self.texto.set("K-means")
        img = self.cv_img
        Z = img.reshape((-1, 3))
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = self.clusters.get()
        ret, label, center = cv2.kmeans(Z, int(K), None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
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
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter widgets y OpenCV")
