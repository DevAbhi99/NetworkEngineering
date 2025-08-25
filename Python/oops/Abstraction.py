# An abstract class can have atleast one abstract method and also if there are multiple abstract method in abstract class then the child class inheriting the abstract class must implement atleast one abstract method


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def horn(self):
        print('Honk!')


class Car(Vehicle):
    def start(self):
        print('Starts with a key')
    
    def stop(self):
        print('Stops with a key')


class Scooty(Vehicle):
    def start(self):
        print('Starts with a kick')
    
    def stop(self):
        print('Stops with a break')


obj1=Car()

obj2=Scooty()

obj1.start()

obj1.stop()

obj2.start()

obj2.stop()