n = int(input())

if n<=9:
    print("0 1 2 3 4 5")
    print("6 7 8 9 0 0")
elif n < 33:
    print("0 1 2 9 4 5")
    print("6 7 8 3 1 2")
else:
    print(-1)