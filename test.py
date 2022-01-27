from PIL import Image, ImageDraw, ImageFont
import sys


with Image.open("background.png") as im:
    fnt = ImageFont.truetype("NikoshBAN.ttf", 85)
    d = ImageDraw.Draw(im)

    d.text((965, 1050), "27/01/22", font=fnt, fill=(0, 0, 0))
    d.text((1470, 1050), "173", font=fnt, fill=(0, 0, 0))
    d.text((1885, 1050), "00", font=fnt, fill=(0, 0, 0))
    d.text((2230, 1050), "13", font=fnt, fill=(0, 0, 0))
    d.text((2585, 1050), "00", font=fnt, fill=(0, 0, 0))
    d.text((2940, 1050), "10", font=fnt, fill=(0, 0, 0))
    d.text((3325, 1050), "08", font=fnt, fill=(0, 0, 0))
    d.text((3900, 1050), "142", font=fnt, fill=(0, 0, 0))


    im.save("test1.png", "PNG")