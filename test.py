#https://github.com/GravenilvecTV/ASCIIArt

from PIL import Image

with Image.open("ppjulien.jpg").convert("RGB") as Image: #.convert("RGB") rajouter suite à erreur int non intenable
    Image = Image.resize((40, 60))

ascii_char = ' .-~=+£@$%§'

for y in range(Image.height):
    line = ""
    for x in range(Image.width):
        rgb = Image.getpixel((x, y))
        grey = sum(rgb) // len(rgb)
        index = grey * 9 // 255
        line += ascii_char[index] + "  "
    print(line)

#écrire dans le terminal  py test.py