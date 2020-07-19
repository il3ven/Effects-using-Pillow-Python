from PIL import Image
import random

# This is the image upon which the effect will be rendered
im = Image.open("assets/eleven-small.jpg")

# Number of frames that will be in the final GIF
NUMBER_OF_FRAMES = 20
# Capture a frame after THRESHOLD number of pixels have been copied
THRESHOLD = (im.size[0] * im.size[1]) / NUMBER_OF_FRAMES

# This is where the magic happens
def shuffleGrid(grid):
    global im
    x_cor = [i for i in range(im.size[0])]
    random.shuffle(x_cor)

    y_cor = [i for i in range(im.size[1])]
    random.shuffle(y_cor)

    for y in y_cor:
        for x in x_cor:
            grid.append((x,y))

gif = []
gif.append(Image.new(im.mode, im.size, color=255))

'''
First a grid is created. Each entry of the grid is a tuple like (x,y)
where x,y are the corresponding coordinates of the pixel.

The effect can be thought as copying pixels from original image to
a new image and capturing the intermediate images to create an effect.

The grid = [] variable decides the order in which the pixels are copied.
'''
grid = []
shuffleGrid(grid)

# Copy pixels in the order defined by grid = []
pixelsWritten = 0
for pixel in grid:
    gif[-1].putpixel(pixel, im.getpixel(pixel))
    pixelsWritten += 1

    if(pixelsWritten > THRESHOLD) :
        pixelsWritten = 0
        gif.append(gif[-1].copy())

# Saving the image as a GIF
gif[0].save('out/noise-effect.gif', save_all=True, append_images=gif[1:], duration=100)

