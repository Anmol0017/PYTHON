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
    def __init__(self, id):
        self.id = id  # Initialize the id attribute
        print(self.id)

class B:
    varB = "Welcome to Class B"

class C(A, B):
    varC = "Welcome to Class C"
    def __init__(self, id):
        super().__init__(id)  # Initialize parent class A

# Creating an instance of C
c1 = C("classID")

print(c1.varA)  # Access from class A
print(c1.varB)  # Access from class B
print(c1.varC)  # Access from class C


# super () method is used to access methods of the
#parent class.


