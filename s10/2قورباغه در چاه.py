t = int(input())

for i in range(t):
    a,b,h = map(int,input().split())
    day = 0
    d=0
    while d<h:
        d+=a
        day+=1
        if d>=h:
            print(day)
            break
        else:
            d-=b
    
        