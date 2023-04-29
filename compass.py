numBearings = int(input())
directions = {"N": 0, "E": 90, "S" : 180, "W": 270}

for bearing in range(numBearings):
    bear = [*(input()[::-1])]
    compass = directions[bear[0]]

    if len(bear) == 1:
        print(compass)
        continue

    for direction in bear[1:]:
        newDirection = directions[direction]
        if compass >= 180 and direction == "N":
            newDirection = 360
        compass = (compass + newDirection) / 2
        print(f"Direction: {direction}, Compass: {compass}")
        
    print(compass)



