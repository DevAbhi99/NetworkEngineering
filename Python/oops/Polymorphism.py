#Polymorphism means many forms. A function with same name can perform different actions

class Calculator:

    def calc(self,x,y=0,z=0):
        if(z!=0):
            print(x*y*z)
        elif(y!=0):
            print(x+y+z)
        else:
            print(x)