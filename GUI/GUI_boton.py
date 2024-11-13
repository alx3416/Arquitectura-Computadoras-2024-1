import tkinter as tk

window = tk.Tk()

button = tk.Button(text="Click me!",
                   width=20,
                   height=8,
                   bg="black",
                   fg="yellow",
                   )
button.pack()

window.mainloop()
