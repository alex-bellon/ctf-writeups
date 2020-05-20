# Uncrackable
## Crypto, ? points

### Prompt

e3f8e5110e29e6fde31a0861f0a4dd13530db5ffdd17113be6c2dd1c022f

### Solution

While the prompt did not provide much guidance, the title reminded me of the fact that the [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) is often referred to as "the Uncrackable Cipher". So I wrote a quick Python script to recover the key that was used, and then XOR it with the ciphertext to get back to the full flag:

```python
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

```

If you run the script, you get the flag: `gigem{blank3t5_g0_1n_cribS_ha}`.
