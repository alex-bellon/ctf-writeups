nums = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'
nums = nums.split(' ')

result = ''
for num in nums:
    if num == '{' or num == '}':
        result += num
    else:
        result += chr(64 + int(num))

print(result)
