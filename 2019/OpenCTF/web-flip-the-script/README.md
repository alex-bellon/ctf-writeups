# Flip the Script
## Web, 64 points

## Prompt

Inject a single JavaScript payload in three contexts: unquoted, in a double-quoted string, and in a single-quoted string.

`challenges.openctf.cat:9001`

## Solution
The challenge was exactly what the prompt said: to make a payload that escaped all three contexts. I didn't have a super intelligent approach to this, just a lot of guessing and checking. In the end, this was the payload that worked:

```JavaScript
/*'/*"+/.*/+target.exploit//
```

The final payload took advantage of commenting and string formatting. Once you passed that to the webpage, it would give you the flag: `flag{whoa_i_am_so_strung_out}`.
