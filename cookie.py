num = input()

while len(num) > 1:
    num = int(num)
    newNum = 0
    while num != 0:
        newNum += num % 10
        num /= 10
        num = int(num)
    num = str(newNum)

print(num)

# wrong answer