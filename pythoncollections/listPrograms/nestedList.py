employees=[
    [100,"tom","developer",25000],
    [101,"john","developer",24000],
    [102,"jack","tester",18000],
    [103,"dain","developer",22000]
]
sum=0
for employee in employees:
    print(employee[1])

for employee in employees:
    if employee[2]=="developer":
        print(employee)

for employee in employees:
    sum=sum+employee[3]
print(sum)


sallist=[]
for employee in employees:
    sallist.append(employee[3])
print("high sal=",max(sallist))

#highsal=0
# for employee in employees:
#     if employee[3]>highsal:
#         highsal=employee[3]