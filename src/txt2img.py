from os import getcwd
from os.path import join
from ArgumentParser import ArgumentParser
from PIL import Image, ImageDraw, ImageFont


def generateImg(text, args):
    colorCodes = {
        "white": (255,255,255),
        "black": (0,0,0),
        "transparent": (0,0,0,0)
    }
    if args.bg == "transparent":
        mode = "RGBA"
    else:
        mode = "RGB"

    fontHeight = int(10 * args.scale)
    font = ImageFont.truetype("../fonts/DejaVuSansMono.ttf", size=fontHeight)


    size = font.getsize_multiline(text)
    print(size)

    bgColor = colorCodes[args.bg]
    img = Image.new(mode, size, bgColor)
    draw = ImageDraw.Draw(img)

    fill = (value:=(255 * (args.bg == "black")), value, value)
    draw.multiline_text((0,0), text, fill=fill, font=font)
    return img
        
def main(args):
    with open(args.i) as textFile:
        text = textFile.read()
    img = generateImg(text, args)
    img.save(args.o)
    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.addArgument("-i", str)
    parser.addArgument("-o", str, default=join(getcwd(), "ASCII.png"))
    parser.addArgument("--bg", str, default="white", choices=["black", "white", "transparent"])
    parser.addArgument("--scale", float, default=3)

    opts = parser.parseArguments()
    main(opts)