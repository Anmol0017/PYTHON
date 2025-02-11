#Static Method
#Methods that dont use the "self" paarmeter 

# we dont need the object in some of the method 
# so we developed statics method

class Student:
    
    name = "anmol"

    # def __init__(self):
    #     pass
    
    @staticmethod
    def hello():
        print("hello world")


s1 = Student()
s1.hello()
print(s1.name)