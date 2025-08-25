from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print('Starts witha key')
    
    def stop(self):
        print('Stops with a key')


class Scooty(Vehicle):
    def start(self):
        print('Starts with a kick')
    
    def stop(self):
        print('Stops with a kick')
