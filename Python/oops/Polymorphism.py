#Polymorphism means many forms

from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calc(self):
        pass


class Sum(Calculator):
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def calc(self):
        return self.x+self.y+self.z


class multiple(Calculator):
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def calc(self):
        return self.x*self.y*self.z
    

class Subtract(Calculator):
    def __init__(self, x,y):
        self.x=x
        self.y=y
    
    def calc(self):
        return self.x-self.y


s=Sum(2,3,4)

m=multiple(2,3,4)

sub=Subtract(9,1)

print(s.calc())

print(m.calc())

print(sub.calc())