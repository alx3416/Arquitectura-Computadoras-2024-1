import tkinter as tk

window = tk.Tk()
window.title('Soy una GUI')

frame1 = tk.Frame(master=window, width=200, height=200, bg="red")
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, width=100, height=100, bg="yellow")
frame2.pack(side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, height=50, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()

# los elementos se dibujan en el orden que se ejecutan las instrucciones PACK
# Al no haber ANCHOR POINT definido, todos los elementos son centrados por default

# Se puede usar comando fill fill=tk.X para rellenar

# SIDE especifica posición dentro de su ventana correspondiente
