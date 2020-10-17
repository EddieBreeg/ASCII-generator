import ArgumentParser
from img2txt import generateText
from txt2img import generateImg
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageOps
from os.path import join
from os import getcwd

def get_args():
    parser = ArgumentParser.ArgumentParser()
    parser.addArgument('-i', str)
    parser.addArgument('-o', str, default=join(getcwd(), "ASCIIGen_out.png"))
    parser.addArgument('--charset', str, default='@%#*+=-:. ')
    parser.addArgument('--res', float, default=2)
    parser.addArgument('--scale', float, default=2.5)
    parser.addArgument('--bg', str, default="white", choices=[
        "white", "black", "transparent"
    ])

    return parser.parseArguments()

def main(args):
    text = generateText(args)
    img = generateImg(text, args)
    img.save(args.o)


if __name__ == '__main__':
    opt = get_args()
    main(opt)
