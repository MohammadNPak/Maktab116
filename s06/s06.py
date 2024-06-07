# # example 2: function with one positional parameter

# # function definition
# def multiply_by_two(x):   # x is function parameter
#       return x*2

# # function cal
# b = multiply_by_two(3)  # 3 is function argument 
# #b -> result is 6.


# # example with two parameter
# def multiply(x,y=1,z=None):
#     if z is None:
#         return x*y
#     else:
#         return x*y*z

# c = multiply(2,7)  # positional argument

# d = multiply(2)
# e = multiply(2,z=10,y=7)
# # f = multiply(x=2,y=6,z=x+y) syntax error


# def sum_of_all(x,y=0,*args):
#     # print(type(args))
#     s=0
#     for z in args:
#         s+=z
#     return s+x+y

# a = sum_of_all(1,2,5,6,8,7,2,9)
# print(a)



# def sum_of_all(x,y=0,**kwargs):
#     print(kwargs)
#     return x+y

# a = sum_of_all(1,2,a=5,b=6,r=8,f=7,key=2,color=9)
# print(a)


# def my_function(**kwargs):
#     for kid in kwargs:
#         print(kid,"last name is ", kwargs[kid])

# # my_function(fname = "Tobias", lname = "Refsnes")

# my_function(mohammad="nozaripak",ali="alavi")
# # {"mohammad":"nozaripak","ali":"alavi"}

# def my_func(positional,*args,keywords,**kwargs):
#     pass

# python modules
    # __builtins__
    # print
    # input
    # tuple

# globals
    # a=10

# none local or closure
    #

# local
    # inside a function


# a = 10
# def myfunc(x,y):
#     return a*(x+y)

# def myfunc2(x,y):
#     global a
#     a=x+y
#     return x+y

# print(myfunc2(1,2))
# print(a)




# import math

# print(dir(math))

# print(math.sin(math.pi/3))



from math import sin,pi
print(sin(pi/3))





