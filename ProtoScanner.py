import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('foto1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Esquinas y donde queremos que se trasladen esos puntos
# 695 33 arriba izq ==> 0,0
# 286 1847 arriba der ==> 0,3456
# 3067 807 abajo izq ==> 4608,0
# 3408,2093 abajo der ==> 4608,3456


rows, cols, ch = img.shape
# puntos para foto 1
pts1 = np.float32([[33, 695], [1847, 286], [807, 3067], [3408, 2093]])  # 4 puntos posicion inicial
pts2 = np.float32([[0, 0], [4000, 0], [0, 6000], [4000, 6000]])  # 4 puntos posicion final

# puntos para foto 2
# pts1 = np.float32([[626, 584], [2393, 545], [690, 3138], [2717, 2977]])  # 4 puntos posicion inicial
# pts2 = np.float32([[0, 0], [4000, 0], [0, 6000], [4000, 6000]])  # 4 puntos posicion final

M = cv2.getPerspectiveTransform(pts1, pts2)
img2 = cv2.warpPerspective(img, M, (4000, 6000))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img2), plt.title('Output')
plt.xticks([]), plt.yticks([])
plt.show()
