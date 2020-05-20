from MegaHash import MegaHash
from random import choice, randrange, seed

ascii = [chr(i).encode('ASCII') for i in range(33, 127)]

found = {}
for j in range(5000):
    s = b''.join([choice(ascii) for _ in range(4)])
    h = MegaHash.hash(s)
    if h in found:
        v = found[h]
        if v == s:
            continue
        print(found[h], s)
    found[h] = s
