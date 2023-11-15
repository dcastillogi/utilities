# Description: This code is used to replace the images in the gallery, for the same images but converted to webp format and named in a sequential way.
# Author: Daniel C. Giraldo
# Date: 08-08-2018
# Version: 1.0
# Python version: 3.6
# Usage: python image.py

# On Debian/Ubuntu: sudo apt-get install webp
# On Mac: brew install webp

import subprocess
import os

PATH = "/home/danielcgiraldo/Desktop/gallery"
QUALITY = "80"
MAX_WIDTH = "800"
START_INDEX = 16


def main():
    images = get_images()

    for index, image in enumerate(images):
        convert_image(image, index + START_INDEX)
        delete_last_image(image)


def get_images():
    return os.listdir(PATH)


def convert_image(img, index):

    subprocess.call(['cwebp', '-q', QUALITY, '-resize', MAX_WIDTH, "0",
                    PATH + "/" + img, '-o', PATH + "/" + str(index) + '.webp'])


def delete_last_image(img):
    os.remove(PATH + "/" + img)


if __name__ == '__main__':
    main()
