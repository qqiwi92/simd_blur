import numpy as np
from PIL import Image
from perf import perf_measure

def run_numpy_optimization():
    img = Image.open('low_q_cat.webp').convert('RGB')
    width, height = img.size
    data = np.array(img, dtype=np.int32)

    KERNEL = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])
    divisor = KERNEL.sum()
    KERNEL_SIZE = 3
    padded = np.pad(data, ((1, 1), (1, 1), (0, 0)), mode='constant')

    with perf_measure("numpy with Cycles"):
        result = np.zeros_like(data, dtype=np.int32)
        for ky in range(KERNEL_SIZE):
            for kx in range(KERNEL_SIZE):
                weight = KERNEL[ky, kx]
                result += padded[ky:ky+height, kx:kx+width] * weight

        result = (result / divisor).clip(0, 255).astype(np.uint8)

    result_img = Image.fromarray(result)
    result_img.save('blurred_cat.webp')

if __name__ == "__main__":
    run_numpy_optimization()