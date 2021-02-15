# //keys id name desig salry
#print employee name
#employee salary



employee={"id":1000,"name":"jino","desig":"eng","salry":32000}
print(employee)

print(employee["name"])
print(employee["salry"])


if "gender" in employee:
    print("entry exist")
else:
    employee["gender"]="male"
print(employee)

employee["salry"]+=5000
print(employee)

for k in employee:
    print(k,",",employee[k])


