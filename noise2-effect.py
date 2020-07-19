'''
This effect is unfinished. For exlpanation see noise-effect.py
'''

from PIL import Image
import random

im = Image.open("assets/eleven-small.jpg")

im_copy = Image.new(im.mode, im.size, color=255)
gif = []
gif.append(im_copy)

BOX_SIZE = 10
numberOfBoxes = (im.size[0]*im.size[1]) // (BOX_SIZE*BOX_SIZE)
grid = []
boxes = list(range(numberOfBoxes))
random.shuffle(boxes)

for pixel in range(BOX_SIZE):
    for j in range(BOX_SIZE):
        grid.append((pixel,j))

for boxIndex in range(numberOfBoxes):
    gif.append(gif[boxIndex].copy())
    offset_x = BOX_SIZE * (boxes[boxIndex] % (im.size[0] // BOX_SIZE))
    offset_y = BOX_SIZE * (boxes[boxIndex] // (im.size[1] // BOX_SIZE))
    random.shuffle(grid)
    for x,y in grid:
        pixel_x = (x+offset_x)%im.size[0]
        pixel_y = (y+offset_y)%im.size[1]
        gif[boxIndex + 1].putpixel((pixel_x, pixel_y), im.getpixel((pixel_x, pixel_y)))

gif[0].save('out/noise2-effect.gif', save_all=True, append_images=gif[1:], duration=0.00001)