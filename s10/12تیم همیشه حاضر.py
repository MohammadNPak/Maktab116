n = int(input())
a = tuple(map(int,input().split()))
distance =dict()


for i,ai in enumerate(a):
    if ai in distance:
        d = i - distance[ai][0]
        if distance[ai][1]<d:
            distance[ai][1]=d
        distance[ai][0]=i
    else:
        distance[ai]=[i,i+1]
        # distance[ai][0]=i
print(min(distance.items(),key=lambda x:max(x[1][1],len(a)-x[1][0]))[1][1])

# 1 2 3 1 3 3 3 3
# n = int(input())
# p = {}
# a = tuple(map(int,input().split()))
# l = len(a)
# for i,ai in enumerate(a):
#     if ai in p:
#         d = i - p[ai]["i"]
#         if d>p[ai]["d"]:
#             p[ai]["d"]=d
#         p[ai]["i"]=i
#     else:
#         p[ai] = {"i":i,"d":i+1}

# for key in p.keys():
#     p[key]["d"] = max(l-p[key]["i"],p[key]["d"])

# print(min([x["d"] for x in p.values()]))