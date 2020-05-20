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
