n = int(input())
for i in range(n-1):
    for j in range(2*n-1):
        if n-1-i == j or n-1+i==j:
            print('D',end="")  
        else:
            print('.',end='')
    print()
for j in range(2*n-1):
    if j%2==0:
        print('D',end="")  
    else:
        print('.',end='')
# n=8
# 0 .......D.......
# 1 ......D.D......
# 2 .....D...D.....
# 3 ....D.....D....
# 4 ...D.......D...
# 5 ..D.........D..
# 6 .D...........D.
# 7 D.D.D.D.D.D.D.D