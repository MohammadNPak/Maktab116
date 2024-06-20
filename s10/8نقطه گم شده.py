# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
cordinates = []
for i in range(7):
    cordinates.append(list(map(int,input().split())))

# cordinates = [[0,0,0],[0,0,1],[0,1,0],[0,1,1]...]

x = [x[0] for x in cordinates] # x=[0,0,0]
y = [x[1] for x in cordinates]
z = [x[2] for x in cordinates]

x_set = {x.count(a):a for a in set(x)}
y_set = {y.count(a):a for a in set(y)}
z_set = {z.count(a):a for a in set(z)}

print(x_set[3],y_set[3],z_set[3])


# how dict comprehension works?

# d = {a:b for a,b in zip(range(8),"mohammad")}
# d={0:"m",1:"o",2:"h",3:"a",4:"m",5:"m",6:"a",7:"d"}