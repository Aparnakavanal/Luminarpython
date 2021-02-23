class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

employees=[]
employees.append(Person(27,"ram"))
employees.append(Person(26,"varun"))
employees.append(Person(24,"nikil"))

for emp in employees:
    if emp.age>25:
        print(emp.name)

empage=[]
for emp in employees:
    empage.append(emp.age)
print(max(empage))

# mx=max(list(map(lambda emp:emp.age,employees)))
# print(ma)








