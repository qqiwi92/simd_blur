from PIL import Image
from perf import perf_measure

def run_flatten_optimization():
    img = Image.open("low_q_cat.webp").convert("RGB")
    width, height = img.size
    
    KERNEL = [1, 2, 1, 2, 0, 2, 1, 2, 1]
    KERNEL_SIZE = 3
    divisor = sum(KERNEL) or 1
    pad = KERNEL_SIZE // 2

    raw_pixels = list(img.get_flattened_data())
    padded_width = width + 2 * pad
    padded_height = height + 2 * pad
    padded_raw = [(0, 0, 0)] * (padded_width * padded_height)

    with perf_measure("Flatten Optimization"):
        for y in range(height):
            for x in range(width):
                padded_raw[(y + pad) * padded_width + (x + pad)] = raw_pixels[y * width + x]

        result_pixels = []
        for y in range(height):
            for x in range(width):
                r_sum, g_sum, b_sum = 0, 0, 0
                for ky in range(KERNEL_SIZE):
                    base_idx = (y + ky) * padded_width + x
                    for kx in range(KERNEL_SIZE):
                        pixel = padded_raw[base_idx + kx]
                        weight = KERNEL[ky * KERNEL_SIZE + kx]
                        r_sum += pixel[0] * weight
                        g_sum += pixel[1] * weight
                        b_sum += pixel[2] * weight

                result_pixels.append((
                    max(0, min(255, int(r_sum / divisor))),
                    max(0, min(255, int(g_sum / divisor))),
                    max(0, min(255, int(b_sum / divisor)))
                ))

    result_img = Image.new("RGB", (width, height))
    result_img.putdata(result_pixels)
    result_img.save("blurred_cat.webp")

if __name__ == "__main__":
    run_flatten_optimization()