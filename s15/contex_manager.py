class MyFile:
    def __init__(self,address) -> None:
        self.address=address
    
    def __enter__(self):
        return f"contex manager was entered"

    def __exit__(self,type, value, traceback):
        if isinstance(value,ZeroDivisionError):
            print("zero division")
            return True
        else:
            print("bye contex manager")


with MyFile("data.txt") as fp:
    print(fp)
    

