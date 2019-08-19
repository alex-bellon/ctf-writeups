# MegaHash 101

## Prompt

I don't know why anyone worries about broken hash algorithms when there are just -so many- of them out there! If you just stack them all together, the flaws in each individual algorithm cover each other. It's basic Defense-in-Depth, and yet the entire cryptographic community never considered it! Introducing the MegaHash cryptographically secure hash algorithm. Basically, I stack together all the available algorithms in a vanilla Python 3.6 instance together in a sequence (a la BlockChain technology). It’s 100% unbreakable unless every single one of them is broken! For your first futile opportunity to get points, implement the easiest of the cryptographic attacks, a collision attack! -- https://en.wikipedia.org/wiki/Collision_attack

`challenges.openctf.cat:9021`

## Solution

As the prompt suggests, the way to break this algorithm -- and I use that term loosely -- was to perform a collision attack. They were even nice enough to link the Wikipedia article!

A collision occurs when to different values result in the same hashed value after a hashing algorithm is applied, and a collision attack tries to force this phenomenon to happen. Collision attacks are most easily done by brute forcing it: generating a bunch of random strings, encoding them with the hashing algorithm, and then keeping track of the results until you get a duplicate. I whipped up a quick Python script to do just that:

```python
from MegaHash import MegaHash
from random import choice, randrange, seed

ascii = [chr(i).encode('ASCII') for i in range(33, 127)] # generate an alphabet of printable characters

found = {}
for j in range(5000):
    s = b''.join([choice(ascii) for _ in range(4)]) # make a random 4 character string
    h = MegaHash.hash(s) # hash the string
    if h in found:
        v = found[h]
        if v == s: # found itself, doesn't count
            continue
        print(found[h], s) # collisions!
    found[h] = s
```

I ran the script, got the two inputs that had a hash collision, entered them into the website and was rewarded with the flag: `flag{with_cryptogr@phy_no_amount_0f_violence_will_3ver_solve_a_math_problem}`.
