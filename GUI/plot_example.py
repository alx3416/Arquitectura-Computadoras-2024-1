import matplotlib.pyplot as plt
import numpy as np

# Generate values for x (from 0 to 2*pi, with small steps)
x = np.linspace(0, 2 * np.pi, 1000)

# Compute the corresponding y values (sine of x)
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Label the axes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Add a title
plt.title('Sine Wave')

# Display the plot
plt.grid(True)
plt.show()
