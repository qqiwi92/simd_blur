import numpy as np
from PIL import Image

img = Image.open('low_q_cat.webp').convert('RGB')
width, height = img.size
data = np.array(img, dtype=np.int32)

KERNEL = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])
divisor = KERNEL.sum()

padded = np.pad(data, ((1, 1), (1, 1), (0, 0)), mode='constant')

result = np.zeros_like(data, dtype=np.int32)

for ky in range(3):
    for kx in range(3):
        weight = KERNEL[ky, kx]
        result += padded[ky:ky+height, kx:kx+width] * weight

result = (result / divisor).clip(0, 255).astype(np.uint8)

result_img = Image.fromarray(result)
result_img.save('blurred_cat.webp')
print("Оптимизация NumPy завершена.")