# Path: files/qr/generate.py

import qrcode
import os

PREFIX = "https://i4s.storend.com.co/vote/"
SUFIX = ""

FILE = "files/qr/list.txt"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=30, # (SIZE)
    border=4,
)

def main():
    # Create output directory
    os.makedirs("files/qr/output", exist_ok=True)

    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()
            qr.add_data(PREFIX + line + SUFIX)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("files/qr/output/" + line + ".png")
            qr.clear()

if __name__ == '__main__':
    main()
