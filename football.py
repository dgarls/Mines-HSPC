numMonths = int(input())

highestPoints = 0
lowestPoints = 10000
highestMonth = 0
lowestMonth = 10000

for mon in range(numMonths):
    month = [int(x) for x in input().split()]
    month = month[1:]

    for score in month:
        if score > highestPoints:
            highestPoints = score
        if score < lowestPoints:
            lowestPoints = score

    total = sum(month)

    if total > highestMonth:
        highestMonth = total
    if total < lowestMonth:
        lowestMonth = total

print(highestPoints)
print(lowestPoints)
print(highestMonth)
print(lowestMonth)
