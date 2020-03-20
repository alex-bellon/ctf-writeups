# SuperCurve
## Crypto, 300 points

### Prompt

We are a super legitimate crypto company asking you to complete an audit on our new elliptic curve, SuperCurve, in order to show those hecklers at WhiteHat how legit we are! `nc crypto.chal.csaw.io 1000`

### Solution

Disclaimer: I don't know anything about Elliptic Curves. But, when I looked through the `server.py` file, I saw that every parameter had a set value except for `secret_scalar`:

```py
secret_scalar = random.randrange(curve.order) # Get random (0, 7919)
```

The range seemed pretty small, so I wrote a script to try all of the possible values:

```py
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
```

And ran it to get the flag: `flag{use_good_params}`
