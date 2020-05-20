import base64
import binascii
import os
import struct

def xorstrings(a, b):
    result = b''
    for i in range(len(a)):
        result += struct.pack("B", (ord(a[i]) ^ ord(b[i])))
    return result

def main():
    a = "¦Òy;dhuÝF]UjhC-1T`h&ÍF1*T{_¦ë¤p02J"
    b = "flag{aaaaaaaaaaaaaaaaaaaaaaaaaaaa}"

    # 10100110 11010010 01111001 00111011 01100100 01101000 01110101 11011101 01000110 01011101 01010101 01101010 01101000 01000011 00101101 00110001 01010100 01100000 01101000 00100110 11001101 01000110 00110001 00101010 01010100 01111011 01011111 10100110 11101011 10100100 01110000 00110000 00110010 01001010

    # 01100110 01101100 01100001 01100111 01111011
    # flag{

    print("a XOR b: " + str(xorstrings(a, b)))

main()
