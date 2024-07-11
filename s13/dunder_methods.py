from typing import Any


class Person:
    __instance=None

    def __new__(cls,name):
        if cls.__instance is None:
            instance = super().__new__(cls)
            cls.__instance=instance
        else:
            instance = cls.__instance
        return instance


    def __init__(self,name) -> None:
        self.name=name

    def __repr__(self) -> str:
        return f"Person(name:{self.name})"
    
    def __str__(self) -> str:
        return f"my name is {self.name}"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.name*args[0]

    def __len__(self):
        return len(self.name)
    
    def __add__(self,other):
        return Person(name=f"{self.name} {other.name}")
    
p = Person("mohammad")
p2 = Person("ali")
# p2.last_name = "nozaripak"

# message = "hello "+str(p)
# print(message)
# print(Person.__mro__)

a = p(2)
print(a)

print(len(p))
# print(p2.last_name)
# print(p.last_name)
# c = p+p2
# print(c)
print(id(p),id(p2))