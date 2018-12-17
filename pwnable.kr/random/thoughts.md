Ok this one is about random values and it's only one point so.... hopefully easy? (famous last words)

SSH in, `ls` and we see `flag`, `random` and `random.c`.

Looking through the file, the program generates a random `unsigned int`, takes in a key, and then checks if the key XOR'd with the random number is `0xdeadbeef`.

I know from past CTFs that randoms are not truly random, something about the same seeds being able to produce the same random number (or something like that). So I'll go off and read the man pages for `rand()` to see if there's anything helpful in there.

Apparently normal `rand` will just produce the same "random" number forever and ever, while `srand()` uses a seed to make a truly random number. I can probably figure out a way to just brute force this and keep trying keys until I get it. There is like a 3000% chance there's a nicer way to do this but that's all I can come up with for now.

Ok, idea. I can just run the program in `gdb` and find the value of the random on the stack. 

Open up `random` in `gdb` and place a breakpoint at the if statement that checks if the `XOR` of `key` and `random` are equal to `0xdeadbeef`. Run it, then show the random number in the stack by typing `x $rbp-0x4`. The random number is `0x6b8b4567` so I just need to find the key. Since `XOR` is its own inverse I can just `XOR` together `0xdeadbeef` and `0x6b8b4567` to get `3039230856`. 

Run `./random` and put in the key to get the flag.
