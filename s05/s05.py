# a = {1,2,10}
# # print(a.count(3))
# b= a
# a.add(100)
# print(a)
# print(b)


# a = (1,2,3)
# print(id(a))
# a = (1,2,3,4)
# print(id(a))
# print(a[2])
# a = [1,2,(3,4)]
# b = [10,20,(3,4)]
# a=2
# b=2
# c=2
# print(id(a),id(b),id(c))


# a=[1,2,3]
# b=a
# c=a.copy()
# print(id(a))
# a.pop()
# print(id(a))
# print(id(b))
# print(id(c))

# a = ["name","age"]
# b  = 0
# c = dict.fromkeys(a,b)
# print(c)
# print(type(c.items()))


a = {'name': "mohammad", 'age': 30}

b = a.popitem()
print(a)
print(b)



# a.update({"job":"engineer"})
# print(a)
# a.popitem()
# print(a)