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
