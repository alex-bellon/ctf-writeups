# The Numbers
## Crypto, ? points

### Prompt

![](the_numbers.png)

### Solution

First, I transcribed the numbers into a text file:

```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}
```

Since all of the numbers were in the 20s or lower, I assumed that these numbers just corresponded to the index of the letter in the alphabet. I made a Python script to convert it:

```python
nums = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'
nums = nums.split(' ')

result = ''
for num in nums:
    if num == '{' or num == '}':
        result += num
    else:
        result += chr(64 + int(num))

print(result)
```

and got the flag: `PICOCTF{THENUMBERSMASON}`.
