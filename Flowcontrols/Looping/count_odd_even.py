limit=int(input("enter limit:"))
i=1
osum=0
esum=0
while(i<=limit):

    if i%2==0:
        esum+=i
    else:
        osum+=i

    i+=1
print("sum of even",esum)
print("sum of odd",osum)
