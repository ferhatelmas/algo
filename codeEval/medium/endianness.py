import sys

if sys.byteorder == "big":
    print "BigEndian"
else:
    print "LittleEndian"
