import binascii
import sys

def calc(msg):
    check = 0
    for i in msg:
        check = AddToCRC(i, check)
    return (check)

def AddToCRC(b, crc):
    if (b < 0):
        b += 256
    for i in range(8):
        odd = ((b^crc) & 1) == 1
        crc >>= 1
        b >>= 1
        if (odd):
            crc ^= 0x8C # this means crc ^= 140
    return crc
