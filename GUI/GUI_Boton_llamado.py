import tkinter as tk

root = tk.Tk()
root.minsize(200, 200)


def onClick(event):
    btn = event.widget  # evento al accionarse un boton n
    print(btn.cget("text"))  # Imprime el numero de boton seleccionado


for i in range(10):
    b = tk.Button(root, text='Button #%s' % i)
    b.grid(row=i, column=0)
    # Bind guardara un valor indicando que boton se accionó
    b.bind("<Button-1>", onClick)

root.mainloop()
