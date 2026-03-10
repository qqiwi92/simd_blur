from PIL import Image

img = Image.open('cat.webp')
img = img.convert('RGB')

KERNEL_SIZE = 3


width, height = img.size

pixels = list(img.get_flattened_data())
matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]


result = list()
for i in range(height - 1 - KERNEL_SIZE):
    for j in range(width - 1 - KERNEL_SIZE):
        resulting_pixel = [0,0,0]
        for inner_x in range(j, j + KERNEL_SIZE):
            for inner_y in range(i, i + KERNEL_SIZE):
                el = matrix[i][j]
                resulting_pixel[0] += 1/9 *el[0]
                resulting_pixel[1] += 1/9 *el[1]
                resulting_pixel[2] += 1/9 *el[2]
        
        
        
        result.append(
            tuple(
                map(int, resulting_pixel)
            )
        )

    if (i % 100 == 0):
        print(i, height)
print(result)