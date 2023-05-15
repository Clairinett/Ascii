#https://github.com/GravenilvecTV/ASCIIArt

from ascii_magic import Image

with Image.open("rickAstley.png").convert("RGB") as Image: #.convert("RGB") rajouter suite à erreur int non intenable
    Image = Image.resize((100, 100))

ascii_char = ' .-~=+£@$%§'

for y in range(Image.height):
    line = ""
    for x in range(Image.width):
        rgb = Image.getpixel((x, y))
        grey = sum(rgb) // len(rgb)
        index = grey * 9 // 255
        line += ascii_char[index] + "  "
    print(line)

#execute  py ascii.py