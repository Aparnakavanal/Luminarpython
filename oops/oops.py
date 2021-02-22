#class
#object
#reference


class Person:
    def set_person(self,age,name):
        self.name=name
        self.age=age

    def print_person(self):
        print(self.name)
        print(self.age)
        print(self.total)

obj=Person()
obj.set_person(25,"ram")
obj.print_person()

obj1=Person()
obj1.set_person(23,"shyam")
obj1.print_person()

