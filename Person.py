class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.__sex="男"

    def whoami(self):
        print("My name is",self.name,self.__gender())

    def myage(self):
        print("I am",self.age,"years old")

    def welcome(self,friend):
        print(self.name,"的朋友是",friend)

    def __gender(self):
        print("性别是",self.__sex)
