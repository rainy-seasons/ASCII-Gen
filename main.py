import os
import sys
from PIL import Image

""" Converts an image to ascii art output as a text file """
""" PIL Docs: https://pillow.readthedocs.io/en/stable/   """

# density string is ordered by "darkest" to "lightest" -> 255-0
DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

img = None

max_size = (128, 128)
input_size = (0, 0)

PixelData = []

def process_file(file):
    if os.path.isfile(file):
        try:
            img = Image.open(file)
            if img.size > max_size:
                img = img.resize(max_size)
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
            print("pixel: {}, {}, = {} | Average: {}".format(x, y, img.getpixel((x, y)), 
                (img.getpixel((x, y))[0] + img.getpixel((x, y))[1] + img.getpixel((x, y))[2]) / 3))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        process_file(sys.argv[1])

    else:
        print("- Pass an image file as an argument -")
