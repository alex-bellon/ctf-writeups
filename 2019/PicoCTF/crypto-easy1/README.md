# Easy1
## Crypto, 100 points

### Prompt

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?

### Solution

You didn't really need the table to solve this, so I just whipped up a Python script to XOR the two strings together:

```python
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
```

I then ran it to get the flag: `picoCTF{MTUFCSQOJHP}`.
