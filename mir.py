import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inpt = input().split()
code = [*inpt[1]]
decoded = ''

for idx, char in enumerate(code):
    newIdx = int(alphabet.index(char) + math.pow(2, idx))
    decoded += alphabet[newIdx % 26]

print(decoded)