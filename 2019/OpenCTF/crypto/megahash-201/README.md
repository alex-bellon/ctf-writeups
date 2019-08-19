# MegaHash 201

## Prompt

Ok, I figured out my problem. As always, the algorithm doesn't fail, it's just an implementation bug in my challenge! I was supposed to be using something called "salt" which I think is like a secret. That makes sense, since I gave you the algorithm, there was nothing secret protecting our password! Well I fixed it. Now we use a standard RFC 2014 HMAC to hash our passwords. The webserver has a random master secret, so even with whatever trick you found you won't know how your submission will be evaluated! Defense-in-depth baby, it never fails!

`challenges.openctf.cat:9024`

## Solution

Ok full disclosure: I never finished that problem. I don't know if that's because my computer wasn't powerful or fast enough to generate the right string in time, or because my approach was wrong (probably the latter). Regardless, let's dive into *trying* to solve the problem.

The prompt mentions that the server is now using an HMAC -- hashed message authentication code -- to try to reduce the chance of a collision. The HMAC algotrithm works by not only hashing the plain text, but also a key/salt. The salt is a random value that should never be reused, and ensures that if you hash the same value two separate times, you will end up with different values (making it harder to determine the plaintext from a hash). In our case, it means we not only have to figure out the plaintext, but the key as well.

The way that the server 

```python
from MegaHash import MegaHash
from random import choice, randrange, seed
import hmac, os

def main():
    target = bytes.fromhex('990acae7ac30911a57f1cd8ddea7afdd38f4ea31afc2467868f71d6166749c547f3d979a169a2a617c2f2b358c480911d31b1bc763ab63193751e699535a4cfd')

    base = hmac.HMAC(bytes.fromhex('405ba28a7a75af3d9d27f9cd2167da9fd44c08db99a9636af143d8b907adfdf7dea49e2b8f25930ed14162d448b1916223a7eb64e0c52729888f629f1d522f60'), digestmod=MegaHash)

    ascii = [chr(i).encode('ASCII') for i in range(33, 127)]

    for a in range(500):
        for j in range(1, 100):
            for i in range(50000):
                s = b''.join([choice(ascii) for _ in range(j)])
                tmpHmac = base.copy()
                tmpHmac.update(s)
                h = tmpHmac.digest()
                if len(h) == len(target):
                    print(str(s) + '\n' + str(h) + '\n')
                    print(str(target) + '\n')
                if h == target:
                    print("FOUND")
                    print(h, s)
                    return

main()
```
