import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca dan ubah ke grayscale
image = cv2.imread('barca.jpg', cv2.IMREAD_GRAYSCALE)

# 2. Threshold agar jadi citra biner
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 3. Structuring element
kernel = np.ones((3,3), np.uint8)

# 4. Operasi morfologi
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

# 5. Tampilkan hasil
titles = ['Original', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
images = [binary, erosion, dilation, opening, closing, gradient]

plt.figure(figsize=(12,6))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()