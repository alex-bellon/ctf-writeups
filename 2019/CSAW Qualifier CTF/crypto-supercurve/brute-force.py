import random
from supercurve import SuperCurve, curve

curve = SuperCurve(
    field = 14753, order = 7919,
    a = 1, b = -1, g = (1, 1),
)

match = input('What is the public key? ')

for secret_scalar in range(curve.order):
    base = curve.g
    pub = curve.mult(secret_scalar, base)
    if(str(pub)) == match:
        print(secret_scalar)
