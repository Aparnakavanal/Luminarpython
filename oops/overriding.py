class Parent:
    def phone(self):
        print("nokia")

class Child(Parent):
    def phone(self):
        print("iphone")

ch=Child()
ch.phone()


#2
class Parent:
    def bike(self):
        print("passion pro")
    def car(self):
        print("alto")

class Child(Parent):
    def bike(self):
        print("re")

ch=Child()
ch.bike()
ch.car()



#3

class Person(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def __str__(self):
        return self.name+str(self.age)

p=Person(25,"ajay")
p1=Person(26,"varun")
print(p)
print(p1)