from PIL import Image

img = Image.open('cat.webp')
img = img.convert('RGB')

KERNEL_SIZE = 3


width, height = img.size

pixels = list(img.get_flattened_data())
matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]

for i in range(height - 1 - KERNEL_SIZE):
    for j in range(width - 1 - KERNEL_SIZE):
        kernel = list()
        for inner_x in range(j, j + KERNEL_SIZE):
            for inner_y in range(i, i + KERNEL_SIZE):
                kernel.append(matrix[i][j])
        print(kernel)
        
            