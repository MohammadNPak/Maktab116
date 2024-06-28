from math import pi
from abc import abstractmethod,ABC
# parent or super class
class Shape(ABC):

    def __init__(self,color) -> None:
        self.color=color
        self.__tickness=10

    def __str__(self) -> str:
        return f"Shape(color:{self.color},tickness:{self.__tickness})"

    @abstractmethod
    def area(self):
        pass

class Material:
    def __init__(self,material) -> None:
        self.material= material


#child or subclass
class Circle(Shape,Material):
    
    def __init__(self, color,material,radius) -> None:
        super().__init__(color)
        Material.__init__(self,material)
        self.radius=radius
    
    def area(self):
        return self.radius**2*pi
    
    # def __str__(self) -> str:
    #     return f"Circle(color:{self.color},tickness:{self.__tickness})"

#child or subclass
class Rectangle(Shape,Material):
    def __init__(self, color,material,height,width) -> None:
        super().__init__(color)
        Material.__init__(self,material)
        self.height=height
        self.width=width

    def area(self):
        return self.height*self.width


# my_shape=Shape("red")
my_circle=Circle("white","paper",10)
my_rect = Rectangle("blue","wood",5,10)

# print(my_shape.color)
print(my_circle.color)
print(my_circle)
# print(my_circle.__tickness)
print(my_rect.color)
print(my_rect.material)
# print(my_rect.area)



print(Shape.__mro__)
print(Circle.__mro__)
print(Rectangle.__mro__)


for obj in (my_circle,my_rect):
    print(obj.area())