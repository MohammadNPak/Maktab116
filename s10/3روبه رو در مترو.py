a = input()  #1 1 0 1 0 0 1 1
b = input()  #1 1 0 0 0 1 0 1



x = 0 
for i,j in zip(a[::2],b[::2]):
    if i=='1'and j=='1':
        x+=1
print(x)




# how zip works
# a = "1 1 0 1 0 0 1 1"
# b = "1 1 0 0 0 1 0 1"
# for k in range(min(len(a),len(b))):
#     i = a[k]
#     j = b[k]
#     pass

# for i,j in zip(a,b):
#     pass
