SSH in, `ls` and see there are 3 files, `flag`, `passcode.c` and `passcode`.

The hint mentions something about a compilation warning, so I'll go ahead and try to compile `passcode.c` and see what it says. Run `gcc passcode.c` and it spits out:

```
passcode.c: In function ‘login’:
passcode.c:9:8: warning: format ‘%d’ expects argument of type ‘int *’, but argument 2 has type ‘int’ [-Wformat=]
  scanf("%d", passcode1);
        ^
passcode.c:14:15: warning: format ‘%d’ expects argument of type ‘int *’, but argument 2 has type ‘int’ [-Wformat=]
         scanf("%d", passcode2);
               ^
```

Alright, so it's passing an `int` instead of an `int pointer`. Not really sure what to do with that information, but I'll keep it in the back of my mind.

Open up `passcode.c` to see what's inside. So it just takes in 2 `ints` and sees if they are `338150` an `13371337` respectively. Ok well when I run it it segfaults after typing the first password, so I need to put in the passwords somehow else.

At this point I got stuck and had to rely on the the much wiser and smarter @Nathan-Huckleberry to talk me through it. He didn't give me the answer (I ain't no cheater) but he did give me some helpful tips about the stack in 32-bit systems, most notably that all arguments, variables, etc. are stored on the stack.
