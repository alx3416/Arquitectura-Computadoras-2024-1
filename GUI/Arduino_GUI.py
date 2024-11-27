import serial
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ArduinoSignalPlotter:
    def __init__(self, serial_port, baud_rate):
        # Set up the serial connection
        self.ser = serial.Serial(serial_port, baud_rate, timeout=1)
        self.signal_data = []

        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title("Arduino Signal Plotter")

        # Create a Matplotlib figure and axis
        self.fig, self.ax = plt.subplots()

        # Create a canvas to embed the plot into the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Start the data reading and plotting loop
        self.read_and_plot()

    def update_plot(self):
        # Update the plot with the latest signal data.
        self.ax.clear()
        self.ax.plot(self.signal_data, label='Signal')
        self.ax.set_ylim([-0.5, 1.5])  # Ensure the y-axis is between 0 and 1
        self.ax.set_title("Signal Plot")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("State")
        self.ax.legend()
        self.canvas.draw()

    def read_and_plot(self):
        # Read data from the serial port and update the plot
        if self.ser.in_waiting > 0:
            data = self.ser.readline().decode('utf-8').strip()  # Read and decode serial data
            print(f"Received: {data}")  # Print the received data (for debugging)

            if data == "turn on":
                self.signal_data.append(1)
            elif data == "turn off":
                self.signal_data.append(0)

            # Update the plot with new data
            self.update_plot()

        # Call this function again after 100ms to continuously check for new data
        self.root.after(100, self.read_and_plot)

    def start(self):
        # start the app
        self.root.mainloop()


# Usage: Create an instance of the ArduinoSignalPlotter class
if __name__ == "__main__":
    serial_port = 'COM3'  # Update this with your Arduino's port
    baud_rate = 9600      # Set the correct baud rate

    plotter = ArduinoSignalPlotter(serial_port, baud_rate)
    plotter.start()
