# Stylist
## Web, 10 points

## Prompt

The prompt was just the `stylist.html` file.

## Solution
When you look at the HTML file, there are a bunch of `div`s that have different colors and `id`s.

```html
<div id="blocks">
  <div id="n11" style="background: #000062;"></div>
  <div id="n29" style="background: #000074;"></div>
  <div id="n26" style="background: #00005f;"></div>
  <div id="n17" style="background: #00006f;"></div>
  .
  .
  .
```

The `n`s in the `id` field made me think that they were indices, and the fact that all the colors only used one byte made me think that they might just be chatacters. I used the magic of multi-cursor editing to get only the indices and hex values:

```
11,62
29,74
26,5f
17,6f
08,5f
20,61
06,68
09,72
14,74
04,7b
27,63
24,72
23,61
10,61
15,5f
01,6c
16,67
03,67
13,69
00,66
02,61
05,74
12,62
28,75
19,5f
22,68
18,74
30,7d
21,5f
07,65
25,65
```

I then wrote a quick Python script to decode and reorder the hex bytes:

```python
import binascii

pairs = open('hex.txt').read()
pairs = pairs[:-1].split('\n')

letters = dict()
for pair in pairs:
    pair = pair.split(',')
    index = int(pair[0])
    letter = binascii.unhexlify(str(pair[1])).decode("utf-8")
    letters[index] = letter

result = ''
for i in range(31):
    result += letters[i]

print(result)
```

When you run it, you get the flag: `flag{the_rabbit_got_a_hare_cut}`.
