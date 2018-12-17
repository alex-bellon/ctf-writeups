1. Open in `gdb` and disassemble main to find the line where the comparison is. Place a breakpoint there.
1. Find where the random is on the stack (in this case rbp-0x4).
1. Run the program, and at the breakpoint run `x $rbp-0x4` to find the random number.
1. `XOR` together the `random` and `0xdeadbeef` to get the key, which in this case is `3039230856`.
1. Run `./random` and type in the key.
