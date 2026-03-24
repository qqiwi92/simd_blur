import numpy as np
from numba import njit, prange
from PIL import Image


@njit(parallel=True, fastmath=True)
def fast_blur(padded_data, kernel, divisor):
    height = padded_data.shape[0] - 2
    width = padded_data.shape[1] - 2
    
    result = np.empty((height, width, 3), dtype=np.uint8)
    
    for y in prange(height):
        for x in range(width):
            r_sum = 0.0
            g_sum = 0.0
            b_sum = 0.0
            
            for ky in range(3):
                for kx in range(3):
                    weight = kernel[ky, kx]
                    pixel = padded_data[y + ky, x + kx]
                    
                    r_sum += pixel[0] * weight
                    g_sum += pixel[1] * weight
                    b_sum += pixel[2] * weight
            
            result[y, x, 0] = min(max(int(r_sum / divisor), 0), 255)
            result[y, x, 1] = min(max(int(g_sum / divisor), 0), 255)
            result[y, x, 2] = min(max(int(b_sum / divisor), 0), 255)
            
    return result
    


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

result = fast_blur(padded, KERNEL, divisor)

result_img = Image.fromarray(result)
result_img.save('blurred_cat.webp')
