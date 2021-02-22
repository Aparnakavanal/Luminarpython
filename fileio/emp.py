employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"raj","desig":"qa","salary":25000},
    1002:{"eid":1002,"ename":"amit","desig":"baa","salary":30000}
}



def print_employee(**kwargs):
    id=kwargs["eid"]

    if id in employees:
        print(employees[id]["ename"])
        if property in kwargs:

            prop=kwargs["property"]
            print(employees[id][prop])
    else:
        print("id not exist")

print_employee(eid=1000,property="salary")
print_employee(eid=1000,property="desig")
