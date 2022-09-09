import imghdr
import struct

import docx2txt

text = docx2txt.process("/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/lab2.docx",
                        '/Users/rahul.madan/PycharmProjects/HackerRank-and-leetcode/img/')


def find_res(filename):
    with open(filename, 'rb') as img_file:  # open image in binary mode
        # height of image is at 164th position
        img_file.seek(163)
        # read the two bytes
        a = img_file.read(2)
        # calculate height
        height = (a[0] << 8) + a[1]
        # read next two bytes which stores the width
        a = img_file.read(2)
        # calculate width
        width = (a[0] << 8) + a[1]
    print("IMAGE RESOLUTION IS : ", width, "X", height)

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return str(width) + "x" + str(height)

for i in range(1, 26):
    try:
        find_res("img/image" + str(i) + ".png")
        print(get_image_size("img/image" + str(i) + ".png"))
    except FileNotFoundError:
        find_res("img/image" + str(i) + ".jpeg")
        print(get_image_size("img/image" + str(i) + ".jpeg"))
