"""
20990
21470
21555
21562
21811
22049
22062
22157
22159
22160
"""

import qrcode
from PIL import Image

def get_data() -> list:
    data = []
    link = "shorturl.at/dfuEU"
    with open('data.txt') as file:
        for line in file:
            data.append([line.strip(), link])
    return data


def generate_qr_codes(data: list):
    for d in data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=16,
            border=6,
        )
        qr.add_data(d[1])
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert('RGB')

        img.save("qr_codes_logo/{}.png".format(d[0]))


if __name__ == '__main__':
    generate_qr_codes(get_data())