import numpy as np
from PIL import Image
from perf import perf_measure

def run_numpy_blur():
    img = Image.open("low_q_cat.webp").convert("RGB")
    data = np.array(img, dtype=np.float32)
    h, w, _ = data.shape

    with perf_measure("NumPy SIMD Optimization"):
        res = (
            data[1:-1, 1:-1] * 4 +
            data[0:-2, 1:-1] * 2 + data[2:, 1:-1] * 2 +
            data[1:-1, 0:-2] * 2 + data[1:-1, 2:] * 2 +
            data[0:-2, 0:-2] + data[0:-2, 2:] +
            data[2:, 0:-2] + data[2:, 2:]
        ) / 16
        
        final = res.clip(0, 255).astype(np.uint8)
        Image.fromarray(final).save("blurred_cat.webp")

if __name__ == "__main__":
    run_numpy_blur()