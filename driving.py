speed = int(input()) * 5280 / 3600
distance = float(input())
time = float(input())

if speed * time > distance:
    print("MADE IT")
else:
    print("FAILED TEST")


