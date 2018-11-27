# -*- coding: utf-8 -*-

import os
import hashlib

def checksum():
    print('Checksum :\r')
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
    

def md5sum():
    print('MD5 :\r')

    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                md5 = hashlib.md5()
                fh = open(f, 'rb')
                # 分批讀取檔案內容，計算 MD5 雜湊值
                for chunk in iter(lambda: fh.read(4096), b""):
                    md5.update(chunk)
                md5data = md5.hexdigest()
                print('{} = 0x{}'.format(f, md5data.upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')


def sha1():
    print('SHA1 :\r')

    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                sha1 = hashlib.sha1()
                fh = open(f, 'rb')
                # 分批讀取檔案內容，計算 MD5 雜湊值
                for chunk in iter(lambda: fh.read(4096), b""):
                    sha1.update(chunk)
                sha1data = sha1.hexdigest()
                print('{} = 0x{}'.format(f, sha1data.upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')


def sha256():
    print('SHA256 :\r')

    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                sha256 = hashlib.sha256()
                fh = open(f, 'rb')
                # 分批讀取檔案內容，計算 MD5 雜湊值
                for chunk in iter(lambda: fh.read(4096), b""):
                    sha256.update(chunk)
                sha256data = sha256.hexdigest()
                print('{} = 0x{}'.format(f, sha256data.upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')


def sha384():
    print('SHA384 :\r')

    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                sha384 = hashlib.sha384()
                fh = open(f, 'rb')
                # 分批讀取檔案內容，計算 MD5 雜湊值
                for chunk in iter(lambda: fh.read(4096), b""):
                    sha384.update(chunk)
                sha384data = sha384.hexdigest()
                print('{} = 0x{}'.format(f, sha384data.upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')


def sha512():
    print('SHA512 :\r')

    for f in os.listdir( ".\\" ):
        try:
            if (f.split('.')[1] == 'rom' or f.split('.')[1] == 'txe' or f.split('.')[1] == 'ME' or f.split('.')[1] == 'me'):
#            if (f.endswith(".rom") or f.endswith(".ROM")):
                sha512 = hashlib.sha512()
                fh = open(f, 'rb')
                # 分批讀取檔案內容，計算 MD5 雜湊值
                for chunk in iter(lambda: fh.read(4096), b""):
                    sha512.update(chunk)
                sha512data = sha512.hexdigest()
                print('{} = 0x{}'.format(f, sha512data.upper()))
                fh.close()
        except (RuntimeError, TypeError, NameError, IndexError):
            pass

    print('\r\n')


if __name__ == "__main__":
    print('\r\n')
    checksum()
    md5sum()
    sha1()
    sha256()
    sha384()
    sha512()
    os.system("pause")
