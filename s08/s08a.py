# a = int(input("enter a: "))
# b = int(input("enter b: "))
# print(a/b)


a = int(input("enter a: "))
b = int(input("enter b: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("b can not be zero!")
    b = int(input("please enter b again: "))
    print(a/b)
except Exception as e:
    print("something wen't wrong")