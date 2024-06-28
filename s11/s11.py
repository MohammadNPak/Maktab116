class MyStudent:
    # class attribute
    eyes_count=2

    def __init__(self,name_,age_,grades_):
        # object attribute
        self.age=age_
        self.grades=grades_
        self.name=name_
    

    # object method
    def greeting(self):
        return f"hello my name is {self.name}"
    
    # class method
    @classmethod
    def show_eyes(cls):
        return f"student eyes are equal to {cls.eyes_count}"

    @staticmethod
    def calculate_mean(list_of_grades):
        return sum(list_of_grades)/len(list_of_grades)
    


# constructor other lan
# initializer  python

s1 = MyStudent("mohammad",20,[17,12,20])

print(s1.age)
s1.age+=1
print(s1.age)



s2 = MyStudent("ali",22,[12,13,14])

print(s2.name)
print(s2.eyes_count)
# MyStudent.eyes_count+=1
print(s2.eyes_count)
print(s1.eyes_count)


# When we call a method of this object as myobject.method(arg1, arg2),
# this is automatically converted by Python into MyClass.
# method(myobject, arg1, arg2) – this is all the special self is about.

print(s1.name,s2.name)

print(s1.greeting())
print(s2.greeting())

print(s1.show_eyes())
print(s2.show_eyes())
print(MyStudent.show_eyes())
# print(s1.show_eyes2())

print(s1.calculate_mean([1,2,3]))


print(s1.eyes_count)
MyStudent.eyes_count+=1
print(s1.eyes_count)
print(s2.eyes_count)