num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))

if(num1>num2)&(num1>num3):
    #num1 high, posibility (num2,num3)
    if(num2>num3):
        print(num2,"is second largest")
        print("sorted order is",num1,num2,num3)
    else:
        print(num3,"is second largest")
        print("sorted order is",num1,num3,num2)

elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"is second largest")
        print("sorted order is",num2,num1,num3)
    else:
        print(num3,"is second largest")
        print("sorted order is",num2,num3,num1)

elif(num3>num2)&(num3>num1):
    if(num2>num1):
        print(num2,"is second largest")
        print("sorted order is ",num3,num2,num1)
    else:
        print(num1,"is second largest")
        print("sorted order is",num3,num1,num2)

elif(num1==num2)&(num2==num3):
    print("3 numbers are equal")

else:
    pass