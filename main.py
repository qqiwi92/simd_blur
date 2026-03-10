from PIL import Image

img = Image.open('cat.webp')
img = img.convert('RGB')

width, height = img.size

pixels = list(img.getdata())
for i in pixels:
    print(i)
