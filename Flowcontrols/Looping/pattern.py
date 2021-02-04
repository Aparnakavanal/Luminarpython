limit=int(input("enter the limit:"))
for i in range(1,limit+1):
    for j in range(0,i):
        print(i,end="")
    print("")

limit=int(input("enter the limit:"))
for i in range(1,limit+1):
    for j in range(0,i):
        print("*",end="")
    print("")


limit=int(input("enter the limit:"))
for i in range(1,limit+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")