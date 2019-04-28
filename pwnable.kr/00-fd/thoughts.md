Go to file descriptor Wikipedia page. 

fds are integers. There are 3 standard ones: 
* 0 (stdin)
* 1 (stdout)
* 2 (stderr)

There's a file table that records the mode in which the file has been opened (read, write, etc).

Ok done reading (see: skimming), ssh in with the given command. 

Log in, ls, there are 3 files: fd, fd.c and flag.

Try to cat flag, can't bc I don't have permission.

Open up fd.c in vim (I copied it into files dir in this repo). It checks that argc >= 2, so I need to pass in some arguments. Then it sets fd to the integer value of argv[1] - 0x1234. Then it calls read().

Google what read() takes as parameters. Ok so it takes in (respectively) a file descriptor, buffer (pointer) to read into, and then the number of bytes to read.

Ok back to the c file, so it's reading 32 bytes from the buffer. If it's the same as "LETMEWIN" it'll give you the flag. 

Getting it now-- it wants me to pass the correct fd in so that I can wrote LETMEWIN in stdin. Need to pass in 0 + the extra 0x1234. Try ./fd 1234 then realize you're dumb and forgot to change it to decimal. Quick Google, find out in decimal 0x1234 is 4660. Try ./fd 4660. Nice, no errors, just blank that I assume is stdin and not something that broke. Type in 'LETMEWIN\n' and it spits out the flag. Nice.
