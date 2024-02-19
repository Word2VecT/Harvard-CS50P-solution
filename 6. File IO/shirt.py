import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    input_extention = os.path.splitext(sys.argv[1])[-1].lower()
    output_extention = os.path.splitext(sys.argv[2])[-1].lower()
    if (input_extention not in [".jpg", ".jpeg", ".png"] or output_extention not in [".jpg", ".jpeg", ".png"]):
        print(input_extention, output_extention)
        sys.exit("Invalid output")
    if (input_extention != output_extention):
        sys.exit("Input and output have different extensions")
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])
        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt) # type: ignore
        photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")