#We are going to learn about classes, contructors and objects 

class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    

    def about(self):
        return 'My name is',self.name,' and my age is', self.age
    



obj=Employee('Karan', 21)


print(obj.about())