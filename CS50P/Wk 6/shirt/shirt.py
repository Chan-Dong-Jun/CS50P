#02/06/2023
#CS50P Week 6

import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Incorrect number of command-line arguments")
if not sys.argv[1].lower().endswith((".png",".jpg",".jpeg")) or not sys.argv[2].lower().endswith((".png",".jpg",".jpeg")):
    sys.exit("Not an image file")
if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Input and output file extensions are different")

shirt = Image.open("shirt.png")
size = shirt.size

try:
    with Image.open(sys.argv[1]) as im:
        im = ImageOps.fit(im, size)
        im.save("a.jpg")
        print(size)
        print(im.size)
        im.paste(shirt,shirt)
        im.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Invalid file")

shirt.close()
