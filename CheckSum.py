# -*- coding: utf-8 -*-

import os

def checksum():
    print('\r\n')
    for root, dirs, files in os.walk("./"):
        for f in files:
            if (f.split('.')[1] == 'TXE' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
                
                fh = open(os.path.join(root, f), 'rb')
                checksum = sum(bytearray(fh.read()))
                print('%s = 0x%s' % (f, format(checksum, '02x').upper()))
                fh.close()
    print('\r\n')
    os.system("pause")

if __name__ == "__main__":
        checksum()