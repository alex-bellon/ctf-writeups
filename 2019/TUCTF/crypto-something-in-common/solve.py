#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com
# This program will help to decrypt cipher text to plain text if you have
# more than 1 cipher text encrypted with same Modulus (N) but different
# exponents. We use extended Euclideangm Algorithm to achieve this.s

import gmpy2

class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0
    def gcd(self, num1, num2):
        if num1 < num2:
           num1, num2 = num2, num1
        while num2 != 0:
           num1, num2 = num2, num1 % num2
        return num1

    def extended_euclidean(self, e1, e2):
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)

    def modular_inverse(self, c1, c2, N):
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m= mx * my % N

    def print_value(self):
        print("Plain Text: ", self.m)

def main():
    c = RSAModuli()
    N = 5196832088920565976847626600109930685983685377698793940303688567224093844213838345196177721067370218315332090523532228920532139397652718602647376176214689
    c1 = 2042084937526293083328581576825435106672034183860987592520636048680382212041801675344422421233222921527377650749831658168085014081281116990629250092000069
    c2 = 199621218068987060560259773620211396108271911964032609729865342591708524675430090445150449567825472793342358513366241310112450278540477486174011171344408
    e1 = 15
    e2 = 13
    c.extended_euclidean(e1, e2)
    c.modular_inverse(c1, c2, N)
    c.print_value()

if __name__ == '__main__':
   main()
