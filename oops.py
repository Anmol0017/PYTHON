class Student:
    collegename= "IIIT" #class attributes
    name = "Anonymus" # for default purpose


    def __init__(self,name,age):
        self.name= name    #object attribute > #class attributes
        self.age= age
    
    def hello(self):  #methods
        print("Welcome Student", self.name)
    def get_age(self):
        return self.age    

s1 = Student("Anmol",23)
print(s1.name," ",s1.age,s1.collegename)
s1.hello()
print(s1.get_age())
print("-----------------------------")
s1.name ="Tony Stark" #we can update from here too
s1.hello()
print(s1.get_age())