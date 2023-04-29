i = [int(x) for x in input().split()]
numPapers = i[0]
numPiles = i[1]
papers = []
for i in range(numPiles):
    papers.append([int(x) for x in input().split()])

numMovements = int(input())

for m in range(numMovements):
    movement = [int(x) for x in input().split()]
    source = movement[0] - 1
    destination = movement[1] - 1
    size = movement[2]
    pile = papers[source][len(papers[source]) - size:]
    del papers[source][len(papers[source]) - size:]
    for num in pile:
        papers[destination].append(num)

for stack in papers:
    if len(stack) == 1:
        print()
        continue
    print(*(stack[1:]))