#Abstraction stands for detail hiding


class Vehicle:
    def __init__(self):
        self.engine=True
    
    def carStart(self):
        print('Car has started')
    
    def carStop(self):
        print('Car has stopped')
    
    def start(self):
        if(self.engine==True):
            self.carStart()
        else:
            self.carStop()



obj=Vehicle()

obj.start()