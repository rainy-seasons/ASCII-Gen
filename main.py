import os
import sys
from PIL import Image, ImageOps
import math

""" USAGE: python main.py (your_image.ext) > output.txt """

# Density string ordered from darkest to lightest.
# Remove some characters for lower resolutions
#DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

img = None

max_size = (128, 128) # Output resolution. More pixels -> More quality
input_size = (0, 0)
ascii_matrix = []

# Initializes the matrix with 0s.
def init_matrix(img):
    for i in range(img.size[0]):
        ascii_matrix.append([])
        for j in range(img.size[1]):
            ascii_matrix[i].append(0)


# Handles basic image operations. resizing -> grayscaling -> calling get_pixel()
def process_file(file):
    if os.path.isfile(file):
        try:
            img = Image.open(file)
            if img.size > max_size:
                img = img.resize(max_size)
            img = ImageOps.grayscale(img) # grayscale the image. Converts (R,G,B) to a single int value.
            init_matrix(img)
            get_pixel(img)

        except OSError:
            print("Cannot process file: '{}'", img)
    else:
        print("File '{}' not found in local directory.".format(file))

# Reads each pixel of the image.
def get_pixel(img):

    # iterate over every pixel
    for x in range(img.width):
        for y in range(img.height):
            percent_of_255 = round(((int(img.getpixel((x, y)))) / 255) * 100) # get the percentage of luminance value out of 255 (max)
            percent_to_index = round((percent_of_255 / 100) * len(DENSITY)-1) # find the corresponding index from the DENSITY string
            pixel_char = DENSITY[percent_to_index]                            # get corresponding value from DENSITY string
            ascii_matrix[y][x] = pixel_char                                   # assign the current position in the matrix with the character

if __name__ == '__main__':
    if len(sys.argv) > 1:
        process_file(sys.argv[1])
        for i in ascii_matrix:
            c = ''.join(x for x in i if x in DENSITY) # Create the string for the current row
            print(c) # print the row
    else:
        print("- Pass an image file as an argument -")
