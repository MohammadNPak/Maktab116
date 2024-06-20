n = int(input())
slices = [float(x) for x in input().split()]
slices.sort()
max_=0
for i in range(1,len(slices)):
    degree = slices[i]-slices[i-1]
    if degree>max_:
        max_=degree

first_slice= slices[0]+(360-slices[-1])
if first_slice>max_:
    max_=first_slice

print(max_/360*100)




# n = int(input())
# degrees = list(map(float,input().split()))
# degrees.sort()

# # print(degrees)
# max_slice = 0
# for i in range(len(degrees)-1):
#     slice = degrees[i+1]-degrees[i]
#     # print(slice)
#     if slice>max_slice:
#         max_slice=slice

# if degrees[0]==0:
#     last_slice = 360-degrees[-1]
# else:
#     last_slice=360-degrees[-1] + (degrees[0]-0)

# if last_slice> max_slice:
#     max_slice=last_slice

# print(max_slice/360*100)