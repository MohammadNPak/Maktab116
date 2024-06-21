import math
from math import gcd

def LCM(a):
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    lcm = LCM((n,k))
    r = math.log2(lcm//n)
    frac=r-int(r)
    if frac!=0:
        print(-1)
    else:
        print(int(r))



# t = int(input())
# li =[]

# def count_two(n:int):
#     counter =0
#     while True:
#         if n%2 ==0:
#             counter +=1
#             n = n/2
#         else:
#             return counter


# def count_num(n:int, k:int):
#     counter =0
#     a =n
#     while True:
#         n = n*2
#         counter +=1
#         if n%k == 0:
#             return counter
#         elif n > k*a+1:
#             return False


# for i in range(t):
#     n ,k = map(int, input().split())

#     if n%k == 0:
#         li.append(0)

#     elif k%n ==0 or k%2==0:
#         c = count_num(n, k)
#         if c == False:
#             li.append(-1)
#         else:
#             li.append(c)

#     else:
#         li.append(-1)


# for i in li:
#     print(i)















# t = int(input())

# reuslt = []
# for i in range(t):
#     cake, guest = (int(num) for num in input().split())
#     while cake % 2 == 0 and guest % 2 == 0:
#         cake /= 2
#         guest /=2
#     cuts = 0
#     while guest % 2 == 0:
#         guest /=2
#         cuts += 1
#     reuslt.append(cuts if cake % guest == 0 else -1)

# for i in reuslt:
#     print(i)        