# Sigma
## Crypto, 145 points

### Prompt

10320831141252164475480592397410881183128414021520157116851780189419421991209921942315241625302578269728072902300131153236334834643575368637343782389340044129

### Solution

Yeah, that was the whole prompt. We noticed that the first 3 numbers, 103, correspond to the decimal ASCII number for 'g'. Since this was the first letter of the flag format, we then realized that the number was the concatentation of the sum of all of the letters before the current one. So the first letter was 'g', the second 'g' + 'i', the third 'g' + 'i' + 'g', and so on. I wrote up a quick Python script to recover the flag:

```python
a = "103208311412521644754805923974"

n = 3
x = [a[i:i+n] for i in range(0, len(a), n)]

print(x)

b = "10881183128414021520157116851780189419421991209921942315241625302578269728072902300131153236334834643575368637343782389340044129"

n = 4
s = [b[i:i+n] for i in range(0, len(b), n)]
print(s)

result = list()
for i in x: result.append(int(i))
for i in s: result.append(int(i))

print(result)

flag = 'g'

for i in range(1, len(result)):
    flag += chr(result[i] - result[i-1])

print(flag)
```

Run the program, get the flag: `gigem{n3v3r_evv3r_r01l_yer0wn_cryptoo00oo}`.
