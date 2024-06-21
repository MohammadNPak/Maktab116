from math import ceil
k = int(input())
n= int(input())
a = list(map(int,input().split()))
a.append(0)

s=0
for i in range(n):
    s+=ceil(abs(a[i+1]-a[i])/k)
s+=ceil(a[0]/k)
s+=n
print(s)
