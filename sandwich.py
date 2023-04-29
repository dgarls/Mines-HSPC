numWords = int(input())


for n in range(numWords):
    word = input().lower()
    word = [*word]

    for char in word:
        if char == 'a' or char == 'b' or char == 'c':
            print(2, end='')
        elif char == 'd' or char == 'e' or char == 'f':
            print(3, end='')
        elif char == 'g' or char == 'h' or char == 'i':
            print(4, end='')
        elif char == 'j' or char == 'k' or char == 'l':
            print(5, end='')
        elif char == 'm' or char == 'n' or char == 'o':
            print(6, end='')
        elif char == 'p' or char == 'q' or char == 'r' or char == 's':
            print(7, end='')
        elif char == 't' or char == 'u' or char == 'v':
            print(8, end='')
        elif char == 'w' or char == 'x' or char == 'y' or char == 'z':
            print(9, end='')
    print()

