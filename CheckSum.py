# -*- coding: utf-8 -*-

import os

def checksum():
    print('\r\n')

#
# Solution 1 : Including all subdirectories
#
#    for root, dirs, files in os.walk(".\\"):
#        for f in files:
#            try:
#                if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#    #            if (f.endswith(".rom") or f.endswith(".ROM")):
#                    fh = open(os.path.join(root, f), 'rb')
#                    checksum = sum(bytearray(fh.read()))
#                    print('{} = 0x{}'.format(f, format(checksum, '02x').upper()))
#                    fh.close()
#            except (RuntimeError, TypeError, NameError, IndexError):
#                pass

#
# Solution 2 : Only search the current directory
#
    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                fh = open(f, 'rb')
                checksum = sum(bytearray(fh.read()))
                print('{} = 0x{}'.format(f, format(checksum, '02x').upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')
    os.system("pause")

if __name__ == "__main__":
        checksum()
