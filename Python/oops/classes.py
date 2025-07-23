class Employee:

    profession="Software Developer"

    def __init__(self, name, salary):   #Creating contructor
        self.name=name
        self.salary=salary
    
    def skills(self):                        #Creating functions
        print("Hi I am a ",self.profession)



#Creating object

obj=Employee("Karan", 45000)

print(obj.name)

print(obj.salary)

obj.skills()

