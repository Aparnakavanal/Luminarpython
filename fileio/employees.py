employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"raj","desig":"qa","salary":25000},
    1002:{"eid":1002,"ename":"amit","desig":"baa","salary":30000}
}

eid=int(input("enter eid"))
property=input("enter property")

if eid in employees:
    print(employees[eid]["ename"])
    if property in employees[eid]:
        print(employees[eid][property])
else:
    print("invalid entry")