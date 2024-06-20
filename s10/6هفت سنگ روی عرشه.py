p = list(map(int,input().split()))
x = int(input())

a = p.index(x)
if a==0:
    print(6)
elif a==6:
    print(1)
else:
    print(7-a)