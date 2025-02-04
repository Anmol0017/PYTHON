class Person:
    #private __ attribute
    __name = "Tony"

    def __hello(self):
        print("hello person",self.__name)
    #public
    def welcome(self):
        self.__hello()

p1 = Person()

p1.welcome()
           