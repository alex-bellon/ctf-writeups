# A Game of Apples
## Misc, 50 points

### Prompt

Wanna play a game? Just a heads up, the bot is really good. If it goes first, it's unbeatable. If you go first, you might have a chance.
`nc 34.74.132.34 1338`

### Solution

After connecting to the given IP, we are prompted with this:

```
→ nc 34.74.132.34 1338
Let's play a simple game, you win if you empty the basket.
Ready?

[+] I go first
The basket has 999 apples
It's my turn. I take 4 apples
The basket has 995 apples
It's your turn. How many apples would you take [1-9]?
9
The basket has 986 apples
It's my turn. I take 4 apples
The basket has 982 apples
It's your turn. How many apples would you take [1-9]?
9
The basket has 973 apples
It's my turn. I take 9 apples
The basket has 964 apples
It's your turn. How many apples would you take [1-9]?
9
The basket has 955 apples
It's my turn. I take 9 apples
The basket has 946 apples
It's your turn. How many apples would you take [1-9]?
.
.
.
```

This goes on for a while, until there are fewer than 10 apples, and odds are the bot takes the remaining apples and wins. There was probably a smarter way to solve this, but it wasn't too much effort to spam `9` and `Enter`, so I kept reconnecting until I made the first move. Then I just kept taking 9 apples until there were fewer than 10. It took a few tries, but eventually:

```
.
.
.
The basket has 37 apples
It's my turn. I take 3 apples
The basket has 34 apples
It's your turn. How many apples would you take [1-9]?
9
The basket has 25 apples
It's my turn. I take 1 apples
The basket has 24 apples
It's your turn. How many apples would you take [1-9]?
9
The basket has 15 apples
It's my turn. I take 7 apples
The basket has 8 apples
It's your turn. How many apples would you take [1-9]?
8
Good job. You won. Here's the flag: CSACTF{0n3_4ppl3_tw0_4ppl3_thr33_4ppl3}
```

I take the last few apples, and get the flag in return: `CSACTF{0n3_4ppl3_tw0_4ppl3_thr33_4ppl3}`.
