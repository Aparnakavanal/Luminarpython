class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp

    # def print_details(self):
    #     print(self.eid,self.name,self.desig,self.sal,self.exp)

    def __str__(self):
        return self.name


f=open("employee","r")
employees=[]

for lines in f:
    eid,ename,desig,sal,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))

for emp in employees:
    print(emp)

sal=[]
for emp in employees:
    sal.append(emp.sal)
print(max(sal),ename)