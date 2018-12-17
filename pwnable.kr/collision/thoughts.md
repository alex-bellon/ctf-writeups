Ok it's talking about MD5 hash collisions, off to Google. 

MD5 is a (defunct) hash function that gives 128-bit hash values. Still used as a checksum, but only against unintentional corruption. Neat.

Apparently it suffers (badly) from hash collisions. HMMMMM. 

Ok skip to "Collision vulnerabilities" section as that seems pretty relevant.

Nevermind, there's a lot of big words there. They have an example of 2 messages with only 6 bit differences. They show that between 2 simliar messages the leading but in each nibble that they changed is flipped (e.g. `0x87` which is `10000111` becomes `00000111` which is `0x07`. So in one message they put the `0x87` in the same spot they put `0x07` in the other message. Don't really know how that contributes to the collisions, but seems important so I'll keep it in mind.

Google MD5 hash collisions, and a lot of spooky math pops up. Time to actually mess with the given server. 

Log in, `ls`, and it's very similar to fd. There's `col`, `col.c` and `flag`. Open `col.c` in vim (and copy it to files dir). 

I need to pass in a string that eventually goes into `check_password`, and once it comes out it needs to be `0x21DD09EC`. Also needs to be 20 bytes. It takes in the password, makes it an array of ints. Then it goes through the array and sums them all up to get the hash. Only does it 5 times though for some reason.

Oh, integers are 4 bytes and chars are 1. So it's treating each 4 char chunk as an int. Cool. Do some math and see that `0x21DD09E` is `568134124` in decimal. Divide that up somewhat evenly into `4 * (113626824) + 113626828` so it's 5 numbers.

After some searching I find that Python has a cool method in the `struct` library called `pack()` that allows you to convert values into byte object. So you can run 
```
4 * struct.pack('<i', 113626824) + struct.pack('<i', 113626828)
``` 
to get what you need. The `<` means little endian and the `i` means convert to the size of the int.

Get the byte code, which is `\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xcc\xce\xc5\x06`. Run 
```
./col $(echo -e "\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xcc\xce\xc5\x06")
``` 
(The `$()` denotes a command and the `-e` flag allows the following to be interperted as hex values.) Get the flag. 

Ok so turns out the whole MD5 thing was completely irrelevant woops. At least I learned something new. Although next time I think I'll start with the problem before diving deeper into the hint/title.
