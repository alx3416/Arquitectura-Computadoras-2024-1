import tkinter as tk

window = tk.Tk()

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=85)
    window.rowconfigure(i, weight=1, minsize=75)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)  # Cada frame es posicionado con GRID
        label = tk.Label(master=frame, text=f"Fila {i}\nColumna {j}")
        label.pack(padx=5, pady=5)  # Cada etiqueta es posicioanda en su respectivo frame con PACK

window.mainloop()

# A pesar de que GRID se usa con frame, la posición de referencia es la ventana principal
