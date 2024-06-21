n,k = map(int,input().split())
a = sorted(map(int,input().split()))

s = 0
for i,f in enumerate(a):
    s+=f+1
    if s>k:
        print(i)
        break
    elif s==k:
        print(i+1)
        break
else:
    print(i+1)


# a = [2,3,1,0,4]
# a.sort()
# a -> [0,1,2,3,4]

# if we want to preserve a
# b = sorted(a)
# a -> [2,3,1,0,4]
# b -> [0,1,2,3,4]