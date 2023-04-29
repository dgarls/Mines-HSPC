import math
from statistics import mean

i = [int(x) for x in input().split()]
numReadings = i[0]
threshold = i[1]

readings = []

for r in range(numReadings):
    readings.append(int(input()))

for groupSize in range(2, numReadings):
    noise = 0
    print("Group size: ", groupSize)
    #Calculate max dif between two adjacent groups
    for i in range(0, numReadings, groupSize):
        if i + groupSize > numReadings - groupSize:
            break
        
        group1 = readings[i:i + groupSize]
        group2 = readings[i + groupSize: i + groupSize + groupSize]
        print(f"Group1: {group1}, group2: {group2}")
        
        mean1 = math.floor(mean(group1))
        mean2 = math.floor(mean(group2))
        
        difference = abs(mean1 - mean2)
        
        print(f"Mean1: {mean1}, Mean2: {mean2}, difference: {difference}")
        
        if difference > noise:
            noise = difference

    print("Noise: ", noise)
    if noise <= threshold:
        print(groupSize)
        break