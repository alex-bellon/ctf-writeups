import struct

def xorstrings(a, b):
    result = b''
    for i in range(len(a)):
        result += struct.pack("B", (ord(a[i]) ^ ord(b[i])))
    return result

def main():

    key = 'SOLVECRYPTO'
    cipher = 'UFJKXQZQUNB'

    print(xorstrings(cipher.lower(), key.lower()).decode('ascii'))

main()
