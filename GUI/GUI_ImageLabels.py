from tkinter import Frame, Button, Label, PhotoImage, Tk
from PIL import Image, ImageTk
from tkinter import filedialog


class GUI(Frame):

    def __init__(self, master=None):
        self.image2 = []
        Frame.__init__(self, master)
        w, h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.choose)
        self.choose = Label(self, text="Choose file")
        self.choose.pack()
        self.image = ImageTk.PhotoImage(Image.open('circles.png'))
        self.label = Label(image=self.image)

        self.file.pack()
        self.label.pack()

    def choose(self):
        path = filedialog.askopenfilename()
        self.image2 = ImageTk.PhotoImage(Image.open(path))
        self.label.configure(image=self.image2)
        self.label.image = self.image2


root = Tk()
app = GUI(master=root)
app.mainloop()
