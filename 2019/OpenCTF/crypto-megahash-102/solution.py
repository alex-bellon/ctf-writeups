from MegaHash import MegaHash
from random import choice, randrange, seed

def main():
    target = bytes.fromhex('6d64392c0c148bb762667c24afcd516a16aa6a05314a0026ad7dd2be29a1dee906780bb2c38fab0350f24dbd5feb5489093e698b578319a0beac3dbcb398efa2')

    ascii = [chr(i).encode('ASCII') for i in range(33, 127)]

    for j in range(1000):
        for i in range(5000):
            s = b''.join([choice(ascii) for _ in range(j)])
            h = MegaHash.hash(s)
            print(s, h)
            print(target)
            print()
            if h == target:
                print("FOUND")
                print(h, s)
                return

main()
