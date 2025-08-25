#Encapsulation stands for data hiding. So a data cannot be tampered but its value can be modified and retreieved

#We are going to encapsulate salary data in Employee class


class Employee:

    def __init__(self):
        self.salary=0

    def setter(self, salary):   #Setter method to updated value
        self.salary=salary
    
    def getter(self):              #Getter method to retrieve the value
        return self.salary
    

obj=Employee()

obj.setter(200000)

print(obj.getter())
