numComputers = int(input())
numFlashes = int(input())
speeds = []

for i in range(numFlashes):
    speeds.append(int(input()))

time = 0
tempSpeeds = []

for speed in speeds:
    tempSpeeds.append(speed)

while numComputers != 0:
    time += 1
    for i in range(len(speeds)):
        tempSpeeds[i] -= 1
        if tempSpeeds[i] == 0:
            numComputers -= 1
            tempSpeeds[i] = speeds[i]

print(time)
# Time limit Exceeded