import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a basic Tkinter window
root = tk.Tk()
root.title("Sine Function Plot")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 4))

# Generate x and y data for the sine function
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Plot the sine function on the axis
ax.plot(x, y, label="y = sin(x)")
ax.set_title("Sine Function")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

# Create a FigureCanvasTkAgg widget to embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the Tkinter main loop
root.mainloop()
