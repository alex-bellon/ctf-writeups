# COBOL OTP
## Crypto, ? points

### Prompt

I don't have the original prompt, but we were given the `cobol_otp` ZIP archive.

### Solution

I didn't actually finish solving this challenge, but I spent a lot of time on it so I wanted to document my progress anyways.

We were given the `otp.cob` file along with the `out` file, which just has the following:
```
Enter your message to encrypt:
���y;dhu��F�]UjhC��-�1T`h&��F�1*T{_���p02J
```

The `otp.cob` file was in COBOL, so I spent a lot of time trying to "translate" it to something I could understand by adding comments (no this is not proper COBOL commenting syntax):

```
identification division.
   program-id. otp.

environment division.
    input-output section.
    file-control.
        select key-file assign to 'key.txt' # keyfile = key.txt
        organization line sequential. # sequential - records are accessed in same order they are inserted

data division.
    file section.
    fd key-file. # file name
    01 key-data pic x(50). # 01 - record description entry, pic x(50) - alphanumeric, 50 bytes

    working-storage section. # temporary vars and file structures
    01 ws-flag pic x(1). # flag is a 1 byte alphanumeric var
    01 ws-key pic x(50). # key is a 50 byte alphanumeric var
    01 ws-parse. # group item
         05 ws-parse-data pic S9(9). # 05 - elementary item in group, S - sign, 9 - number, of length 9
    01 ws-xor-len pic 9(1) value 1. # xor-len is a 1 byte number = 1
    77 ws-ctr pic 9(1). # ctr is 1 byte number

procedure division.
    open input key-file.
    read key-file into ws-key end-read. # key = read(key-file)

    display 'Enter your message to encrypt:'.
    move 1 to ws-ctr. # ctr++
    perform 50 times
        call 'getchar' end-call
        move return-code to ws-parse # parse = getchar
        move ws-parse to ws-flag # flag = parse

        call 'CBL_XOR' using ws-key(ws-ctr:1) ws-flag by value # flag = xor(key[ctr], flag) limited to 1 byte (xor-len)
        ws-xor-len end-call

        display ws-flag with no advancing # print(flag, separator='')
        add 1 to ws-ctr end-add # ctr++
    end-perform.

cleanup.
    close key-file.
    goback.
end program otp.
```

This was kind of useless, since it turned out to be -- shockingly -- a one time pad! I then wrote a quick Python program to try to decode it using a known plaintext attack:

```python
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
```
This is where I got stuck, as the output of this program was just gibberish. Oh well :(.
