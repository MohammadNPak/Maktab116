from datetime import date
import csv


class Student:

    data_address: str = ""
    encoding: str = ""

    def __init__(self, id: int, name: str, birth_date: date, grades: list[float]):
        # object attribute
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.grades = grades

    @classmethod
    def set_data_address(cls, address):
        cls.data_address = address

    @classmethod
    def set_encoding(cls, encoding):
        cls.encoding = encoding

    def save(self):
        with open(self.data_address, "a",encoding=self.encoding) as fp:
            writer = csv.DictWriter(fp, ["id", "name", "birth_date", "grades"])
            writer.writerow({
                "id": self.id,
                "name": self.name,
                "birth_date": self.birth_date,
                "grades": self.grades}
            )

    @classmethod
    def get(cls,id):
        with open(cls.data_address, "r",encoding=cls.encoding) as fp:
            reader = csv.DictReader(fp, delimiter=',')
            for line in reader:
                if line["id"]==str(id):
                    return line


Student.set_data_address("data.csv")
Student.set_encoding("utf-8")


# s1 = Student(1,"mohammad",date(1991,3,23),[20,19,18])
# s1.save()
# my_student = Student.get(id=1)
# print(my_student)

while True:
    command = input("enter your command: ")
    if command=="new":
        id,name,year,month,day,*grades = input("please enter student attribute: id,name,year,month,day,*grades").split()
        s = Student(int(id),name,date(int(year),int(month),int(day)),grades)
        # print(s.name)
        s.save()
    elif command=="get":
        print(Student.get(input("please enter student id: ")))
    elif command=="exit":
        print("goodbye")
        break

