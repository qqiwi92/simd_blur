from PIL import Image

img = Image.open("low_q_cat.webp")
img = img.convert("RGB")
width, height = img.size

KERNEL = [1, 2, 1, 2, 0, 2, 1, 2, 1]


KERNEL_SIZE = 3

divisor = sum(KERNEL)
if divisor == 0:
    divisor = 1

pad = KERNEL_SIZE // 2

raw_pixels = list(img.get_flattened_data())

padded_width = width + 2 * pad
padded_height = height + 2 * pad
padded_raw = [(0, 0, 0)] * (padded_width * padded_height)

result_pixels = []
for y in range(height):
    for x in range(width):
        padded_raw[(y + pad) * padded_width + (x + pad)] = raw_pixels[y * width + x]

for y in range(height):
    for x in range(width):
        r_sum, g_sum, b_sum = 0, 0, 0

        for ky in range(KERNEL_SIZE):
            for kx in range(KERNEL_SIZE):
                pixel = padded_raw[padded_width * (y + ky) + (x + kx)]
                weight = KERNEL[ky * KERNEL_SIZE + kx]

                r_sum += pixel[0] * weight
                g_sum += pixel[1] * weight
                b_sum += pixel[2] * weight

        r_final = max(0, min(255, int(r_sum / divisor)))
        g_final = max(0, min(255, int(g_sum / divisor)))
        b_final = max(0, min(255, int(b_sum / divisor)))

        result_pixels.append((r_final, g_final, b_final))

result_img = Image.new("RGB", (width, height))
result_img.putdata(result_pixels)
result_img.save("blurred_cat.webp")
