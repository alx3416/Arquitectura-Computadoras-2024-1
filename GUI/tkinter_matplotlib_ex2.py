import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Function to update the plot based on the slider value
def update_plot(val):
    frequency = float(val)  # Get the frequency from the slider value

    # Recalculate the y values based on the new frequency
    y = np.sin(frequency * x)

    # Clear the current plot and plot the updated sine function
    ax.clear()
    ax.plot(x, y, label=f"y = sin({frequency} * x)")
    ax.set_title("Sine Function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # Redraw the canvas
    canvas.draw()


# Create the Tkinter window
root = tk.Tk()
root.title("Sine Function Plot with Frequency Control")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 4))

# Generate x data (constant, doesn't change)
x = np.linspace(0, 2 * np.pi, 100)

# Set an initial frequency
initial_frequency = 1.0

# Generate initial y data for the sine function with the initial frequency
y = np.sin(initial_frequency * x)

# Plot the initial sine function
ax.plot(x, y, label=f"y = sin({initial_frequency} * x)")
ax.set_title("Sine Function")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

# Create a FigureCanvasTkAgg widget to embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create a slider to adjust the frequency of the sine wave
slider = tk.Scale(root, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL,
                  label="Frequency", command=update_plot)
slider.set(initial_frequency)  # Set initial value
slider.pack(fill=tk.X, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
