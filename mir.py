import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inpt = input().split()
code = [*inpt[1]]

for idx, char in enumerate(code):
    newIdx = int(alphabet.index(char) + math.pow(2, idx))
    print(alphabet[newIdx % 26], end='')

# Wrong answer