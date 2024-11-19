import numpy as np
import matplotlib.pyplot as plt

# Define the parameters u and v
u = np.linspace(0, 4 * np.pi, 100)  # u parameter (angle)
v = np.linspace(-2, 2, 10)  # v parameter (height)

# Create meshgrid for u and v
u, v = np.meshgrid(u, v)

# Parametric equations for the helicoid
x = np.cos(u)
y = np.sin(u)
z = v

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Helicoidal Surface')

# Display the plot
plt.show()
