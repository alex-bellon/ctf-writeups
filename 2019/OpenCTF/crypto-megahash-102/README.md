# MegaHash 102
## Crypto, 52

## Prompt

How'd you do that??? Well, there's no way you could extend that all the way to a full preimage attack! -- https://en.wikipedia.org/wiki/Preimage_attack

`challenges.openctf.cat:9022`

## Solution

Again, this problem is pretty straight-forward, as the solution strategy is given right in the prompt: a preimage attack.

A preimage attack is very similar to a collision attack, but instead of trying to get *any* two strings to have a hash collision, you are already given one of the strings that you want to have a hash collision with. This means that you already know the hash that you are looking for.

Since the attack is pretty similar, so was the script: generate a bunch of random strings, apply the hashing algorithm, and compare the resulting hash to the target hash to see if they match. I also made the string be of variable length, rather than just 4, so the chances of finding a match would be higher:

```python
from MegaHash import MegaHash
from random import choice, randrange, seed

def main():
    target = bytes.fromhex('6d64392c0c148bb762667c24afcd516a16aa6a05314a0026ad7dd2be29a1dee906780bb2c38fab0350f24dbd5feb5489093e698b578319a0beac3dbcb398efa2') # target hash

    ascii = [chr(i).encode('ASCII') for i in range(33, 127)] # generate an alphabet of printable characters

    for j in range(1000):
        for i in range(5000):
            s = b''.join([choice(ascii) for _ in range(j)]) # generate a random string of length 'j'
            h = MegaHash.hash(s) # hash the string
            if h == target: # collision!
                print("FOUND")
                print(h, s)
                return

main()
```

Run the script, get the string that creates a collision, plug it into the website, and get the flag: `flag{2nd_preimages_4_fun_&_pr0fit}
`.
