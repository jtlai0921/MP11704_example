import sys
import zlib
import os.path

filename = sys.argv[1]
if os.path.isfile(filename):
    fp = open(filename, 'rb')
    contents = fp.read()
    fp.close()
    print(zlib.crc32(contents.encode()))
else:
    print('file not exists')
