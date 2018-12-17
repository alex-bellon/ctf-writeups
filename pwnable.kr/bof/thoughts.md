A buffer overflow problem, something I *actually* know a little about.

Ok it takes from stdin so I need to get all the bytes written out so I can copy-paste them. Open Python and run:
```
import struct
32 * struct.pack('B', 255)
```
`B` is for `unsigned char`. Dont need `<` since endianness doesn't matter here. Honestly, whatever you put in there doesn't matter. Just need 32 bytes of something. Copy the `\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff` and go to put it into `buf`.

I went on to mess around a bunch with trying to overflow the buffer and got nowhere. I know its some kind of issue with the fact that 32-bit registers are passed on the stack and so I either need to overflow more or less than the 32 bytes. I don't want to go into gdb *just* yet, so I start Googling around and find pwntools, which will probably make this a lot faster.

Write up a Python script to connect and overflow the buffer (see `bof.py`). Not working with a buffer of 32, so look like I need to dive into gdb anyways. 

After a little bit of messing around found that the offset is 52. Changed Python file accordingly, run, `cat flag` and done.
