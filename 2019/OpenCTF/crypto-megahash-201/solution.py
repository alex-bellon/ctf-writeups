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
