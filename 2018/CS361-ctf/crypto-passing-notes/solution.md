# Passing Notes

This is a Diffie-Hellman Key Exchange. I wrote the following script to solve it:

```
mod = 0x10abd6bdefdc9f8dfca4ce12d50a29814d4c3d
base = 0x2

m1str = 'banana'
m2str = 'apple'

m1 = m1str.encode('ascii').hex()
m2 = m2str.encode('ascii').hex()

#https://www.alpertron.com.ar/DILOG.HTM
a = 305029171471118065346586662956664018796828610
b = 247579475232354162118808665013791093677258034

print(m1)
print(m2)

key = pow(base, (a * b), mod)
print(key)

message = 0xd7beb91bdc4e7db78656d7c8312a151c77cad
message = hex((message ^ key))

print(message)

message = bytes.fromhex(message[2:len(message)]).decode('ascii')
print(message)
```

