class Employee:

    def __init__(self):
        self.salary=0
    

    def setter(self, salary):
        self.salary=salary
    
    def getter(self):
        return self.salary


obj=Employee()

obj.setter(1000000)

print(obj.getter())