from PIL import Image

img = Image.open('low_q_cat.webp')
img = img.convert('RGB')

KERNEL_SIZE = 10

width, height = img.size

new_width = width - 1 - KERNEL_SIZE
new_height = height - 1 - KERNEL_SIZE


pixels = list(img.get_flattened_data())
matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]


result = list()
result_img = Image.new('RGB', (new_width, new_height))

divisor  = KERNEL_SIZE * KERNEL_SIZE
for i in range(height - 1 - KERNEL_SIZE):
    for j in range(width - 1 - KERNEL_SIZE):
        r_sum, g_sum, b_sum = 0, 0, 0
        for k_x in range(j, j +  KERNEL_SIZE):
            for k_y in range(i, i +  KERNEL_SIZE):
                pixel = matrix[k_y][k_x]
                r_sum += pixel[0]
                g_sum += pixel[1]
                b_sum += pixel[2]



        result.append((
                    int(r_sum / divisor),
                    int(g_sum / divisor),
                    int(b_sum / divisor)
                ))

    # if (i % 10 == 0):
    #     print(i, height)

result_img.putdata(result)

result_img.save('blurred_cat.webp')
result_img.show()
