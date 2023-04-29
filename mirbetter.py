total_input = input()
total_input = total_input.upper()
cypher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
res = []
word = []
rep = ''
w = 0
for i in total_input:
    if i.isnumeric():
        res.append(i)
    else:
        word.append(i)
while w < 2:
    rep += res.pop(0)
    w +=1
del word[0]

i = 0
final = ""
for x in word:
    for idx, c in enumerate(cypher):
        if x == c:
            final += cypher[(idx+2**i) % 26]
            i +=1
print(final)