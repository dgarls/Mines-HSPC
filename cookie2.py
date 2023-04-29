def getTotal(num):
    num = [*num]
    num = [int(x) for x in num]
    total = sum(num)
    return total

num = input()

while len(num) > 1:
    num = str(getTotal(num))
print(num)