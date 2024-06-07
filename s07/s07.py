# print(dir(__builtins__))

# a=5
# b=2
# def add(x,y,*args):
#     return sum(args)+x+y

# a = sum([2,3,4])
# print(a)  # 2+3+4-> 9

# def add2(x,y,*args):
#     s=0
#     for i in args:
#         s+=i
#     print(locals())
#     return s+x+y

# # print(globals())

# print(add2(2,1))
# print(built)



def welcome():
    a=0
    def helper(name):
        nonlocal a
        a+=1
        print("welcome"+name)
        print(a)
    return helper



if __name__=="__main__":
    a=0
    welcome("mohammad")
    welcome("ali")
    welcome("ahmad")
    print("s07")
    print(__name__)
