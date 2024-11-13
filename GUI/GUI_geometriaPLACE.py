import tkinter as tk

# Con PLACE las coordenadas están en pixeles

window = tk.Tk()

frame = tk.Frame(master=window, width=250, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="Estoy en la posición (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="Estoy en la posición (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()

# Interfaces con PLACE no pueden tener resize automatico con el cambio de ventana
