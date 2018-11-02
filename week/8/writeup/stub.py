#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def not_ascii(inp):
    for c in inp:
        if c < 0 or c > 127:
            return True
    return False
    
# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1
SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x3
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
index = 0
offset = 12
magic, version, timestamp = struct.unpack("<LLL", data[index:offset])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestr = str(int(timestamp))

if len(timestr) != 10:
    bork("Invalid timestamp, length was not 10")

index = offset
offset += 8

author = data[index:offset]

if not not_ascii(author):
    bork("Invalid author field")

#dealing with the null padding

index = offset
offset += 4

sec_num = struct.unpack("<L", data[index:offset])[0]

if int(sec_num) < 0:
    bork("Invalid section number")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.utcfromtimestamp(int(timestr)))
print("AUTHOR: %s" % author.decode("ascii"))
print("SECTIONS: %d" % int(sec_num))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
print("-------  BODY  -------")

while offset < len(data):
    index = offset
    offset += 8

    s_type,s_len = struct.unpack("<LL", data[index:offset])

    print("TYPE: %s" % int(s_type))
    print("LENGTH: %d" % int(s_len))
    index = offset
    offset += s_len
    s_t = data[index:offset]

    if s_type == SECTION_PNG:
        if not len(s_t) == s_len:
            bork("Invalid PNG")
        print("IMAGE Found")
        fout = open("embedded" + str(index)+ ".png", 'w')
        fout.write(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
        fout.write(s_t)
        print("------------------------------")
    elif s_type == SECTION_DWORDS:
        if not len(s_t) % 8 == 0:
            bork("Invalid Dwords Section")
        arr = struct.unpack('<' + 'Q'*int(len(s_t)/8), s_t)
        for n in arr:
            print('%d' % int(n))
        print("------------------------------")
    elif s_type == SECTION_UTF8:
        if not len(s_t) == s_len:
            bork("Invalid UTF")
        print("Text: %s" % s_t.decode("utf-8"))
        print("------------------------------")
    elif s_type == SECTION_DOUBLES:
        if not len(s_t) % 8 == 0:
            bork("Invalid Doubles Section")
        arr = struct.unpack('<' + 'd'+int(len(s_t)/8), s_t)
        for n in arr:
            print('%f' % float(n))
        print("------------------------------")
    elif s_type == SECTION_WORDS:
        if not len(s_t) % 4 ==  0:
            bork("Invalid Words Section")
        arr = struct.unpack('<' + 'L'*int(len(s_t)/4), s_t)
        for n in arr:
            print('%d' % int(n))
        print("------------------------------")
    elif s_type == SECTION_COORD:
        #valid coordinates
        lat,lon = struct.unpack('<dd', s_t)
        if not len(s_t) == 16:
            bork("Invalid Coordinates")
        print('%f' % lat)
        print('%f' % lon)
        print("------------------------------")
    elif s_type == SECTION_REFERENCE:
        #must be a word
        if not len(s_t) == 4:
            bork("Invalid Reference")
        arr = struct.unpack('<L', s_t)[0]
        print(str(int(arr)))
        print("------------------------------")
    elif s_type == SECTION_ASCII:
        #must be slen bytes of text
        if not len(s_t) == s_len:
            bork("Invalid ascii")
        print("Text: %s" % s_t.decode("ascii"))
        print("------------------------------")
    else:
        bork("invalid section")
        print("------------------------------")
