class Student():
    def set_std(self,rollnum,name,total):
        self.rollnum=rollnum
        self.name=name
        self.total=total

    def print_std(self):
        print(self.rollnum)
        print(self.name)
        print(self.total)

obj=Student()
obj.set_std(1,"aashu",50)
obj.print_std()

obj1=Student()
obj1.set_std(2,"fari",53)
obj1.print_std()