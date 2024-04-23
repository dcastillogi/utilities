# Description: This code is used to replace file names in a directory with a sequence.
# Author: Daniel C. Giraldo
# Date: 01-04-2024
# Version: 1.0
# Python version: 3.6
# Usage: python main.py

import os

PATH = "/Users/danielcastillo/Downloads/podso previews"
NAME_METHOD = "random" # random or sequential

def get_files():
    return os.listdir(PATH)


def main():
    files = get_files()
    for index, file in enumerate(files):
        if NAME_METHOD == "sequential":
            new_name = str(index) + os.path.splitext(file)[1]
        elif NAME_METHOD == "random":
            new_name = str(index) + os.urandom(4).hex() + os.path.splitext(file)[1]
        os.rename(PATH + "/" + file, PATH + "/" + new_name)
    


if __name__ == '__main__':
    main()
