#-----------------------
#single level inheritance
#-----------------------
class Car: # single parent class

    color ="black"


    @staticmethod
    def start():
        print("carr started...")

    @staticmethod
    def stop():
        print("carr stopped...")

class ToyotaCar(Car):  #single child class 
    def __init__(self,name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("nano")

print(car1.start())
print(car2.color)


#-----------------------
#multi level inheritance
#-----------------------
class A:
    varA = "Welcome to Class A"
class B(A):
    varB="welcome to class B"

class C(B):
    varC = "welcome to class C"    

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)



#-----------------------
#multiple inheritance
#-----------------------
class A:
    varA = "Welcome to Class A"
class B:
    varB="welcome to class B"

class C(A,B):
    varC = "welcome to class C"    

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


