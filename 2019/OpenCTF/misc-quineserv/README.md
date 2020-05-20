# Quineserv
## Miscellaneous, 64 points

## Prompt

Electric Frankenstein wrote this service. I think it is going a little too far into Gödel Escher Bach if you ask me. But at least it tells you when you accidentally infect the laboratory with a virus.

`challenges.openctf.cat:9006`

## Solution

I honestly had no idea what the prompt was talking about, but when you connected to that server, it would take input. I assumed that it was looking for a valid [quine](https://en.wikipedia.org/wiki/Quine_%28computing%29), so I went online and found a pretty simple Python one:

```python
s = 's = %r; print (s%%s)'; print (s%s)
```

I submitted it to the server and got the flag in return: `flag{If only one of us could find the time. adeb4289b6a555}`.
