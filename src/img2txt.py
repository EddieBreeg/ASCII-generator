import ArgumentParser
from cv2 import imread, cvtColor, COLOR_BGR2GRAY
from PIL import ImageFont
import numpy as np
from os import getcwd
from os.path import join

def get_args():
    parser = ArgumentParser.ArgumentParser()
    parser.addArgument("-i", str)
    parser.addArgument('-o', str, default=join(getcwd(), "ASCIIGen_out.txt"))
    parser.addArgument('--charset', str, default='@%#*+=-:. ')
    parser.addArgument("--res", float, default=1)
    return parser.parseArguments()

def generateText(opt):
    CHAR_LIST = opt.charset
    num_chars = len(CHAR_LIST)
    
    cell_height = int(50 / opt.res)
    font = ImageFont.truetype("../fonts/DejaVuSansMono.ttf", size=cell_height)
    cell_width, cell_height = font.getsize(' ')

    image = imread(opt.i)
    image = cvtColor(image, COLOR_BGR2GRAY)
    
    height, width = image.shape
    num_cols = int(width / cell_width)
    num_rows = int(height / cell_height)


    output_text = ""
    for i in range(num_rows):
        for j in range(num_cols):
            output_text += (
                CHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                          int(j * cell_width):min(int((j + 1) * cell_width),
                                                                  width)]) * num_chars / 255), num_chars - 1)])
        output_text+='\n'
    return output_text

def main(opt):
    output_file = open(opt.o, 'w')
    output_file.write(generateText(opt))
    output_file.close()


if __name__ == '__main__':
    opt = get_args()
    main(opt)
