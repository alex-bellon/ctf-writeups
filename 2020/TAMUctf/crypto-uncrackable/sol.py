import base64
import binascii
import os
import struct

def main():
    a = str.encode('gigem{')
   
    cipher = "e3f8e5110e29e6fde31a0861f0a4dd13530db5ffdd17113be6c2dd1c022f"
    cipher = bytes.fromhex(cipher)

    print(a)
    print(cipher)

    result = list()
    for i in range(len(a)):
        letter = a[i] ^ cipher[i]
        result.append(letter)

    pad = result + result + result + result + result

    result = ''
    for i in range(len(cipher)):
        letter = pad[i] ^ cipher[i]
        result += chr(letter)
    print(result)

main()
