n = int(input())
positions=dict.fromkeys(range(1,4),0)
positions[1]=1

for i in range(n):
    a,b = map(int,input().split())
    positions[a],positions[b]=positions[b],positions[a]

print([key for key,value in positions.items() if value==1][0])


# n = int(input())

# command = []
# for _ in range(n):
#     command.append([int(x) for x in input().split()])

# pea =1
# for c in command:
#     if c[0]==pea:
#         pea=c[1]
#     elif c[1]==pea:
#         pea=c[0]
# print(pea)