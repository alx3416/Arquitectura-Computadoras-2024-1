import numpy as np
import matplotlib.pyplot as plt

# === Datos de entrenamiento ===
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# === ENTRENAMIENTO ===
x_mean = np.mean(x)
y_mean = np.mean(y)

x_diff = x - x_mean
y_diff = y - y_mean

m = np.sum(x_diff * y_diff) / np.sum(x_diff ** 2)
b = y_mean - m * x_mean

# === RESULTADOS DEL ENTRENAMIENTO ===
print(f"Pendiente (m): {m:.3f}")
print(f"Intercepto (b): {b:.3f}")

# === PREDICCIÓN DE LA RECTA ===
x_linea = np.linspace(min(x), max(x), 100)  # muchos puntos para la recta
y_linea = m * x_linea + b

# === GRAFICAR ===
plt.scatter(x, y, color='blue', label='Datos observados')  # puntos originales
plt.plot(x_linea, y_linea, color='red', label='Recta ajustada')  # recta del modelo
plt.title('Regresión Lineal Simple')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
