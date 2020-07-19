import io
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 20
CURSOR_WIDTH = 5
CURSOR_HEIGHT = FONT_SIZE

def createBanner(stream: io.BytesIO):
    text = "Hi, You awesome human."
    gif = []
    pixel = [10, 10]
    fnt = ImageFont.truetype("assets/Roboto-Regular.ttf", FONT_SIZE)

    prev_im = Image.new("RGB", (400, 50), (255,255,255))

    # Add a character and copy image to gif = []
    for i in range(len(text)):
        temp_im = prev_im
        d = ImageDraw.Draw(temp_im)
        d.text(tuple(pixel), text[i], font=fnt, fill=(0, 0, 0))
        size = d.textsize(text[i], font=fnt)
        pixel[0] += size[0]
        prev_im = temp_im.copy()
        d.rectangle([pixel[0], pixel[1], pixel[0]+CURSOR_WIDTH, pixel[1]+CURSOR_HEIGHT], fill=(0,0,0)) # For the typing cursor
        gif.append(temp_im)
    
    gif[0].save(stream, format="GIF", save_all=True, append_images=gif[1:], duration=100)
    return

f = open("out/typing-effect.gif", "wb")
createBanner(f)
f.close()

# ALTERNATIVE IN MEMORY SOLUTION
# f = io.BytesIO()
# createBanner(f)
# f.seek(0)
# f is byte stream which can be sent for example as an HTTP response