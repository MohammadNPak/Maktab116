n = int(input())

result =[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    if a+c > b+d:
        result.append("perspolis")
    elif a+c < b+d:
        result.append("esteghlal")
    else:
        if c>b:
            result.append("perspolis")
        elif c<b:
            result.append("esteghlal")
        else:
            result.append("penalty")

for r in result:
    print(r)