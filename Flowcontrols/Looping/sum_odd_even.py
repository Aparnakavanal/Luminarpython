limit=int(input("enter limit:"))
i=1
ocount=0
ecount=0
while(i<=limit):

    if i%2==0:
        ecount+=1
    else:
        ocount+=1

    i+=1
print("count of even",ecount)
print("count of odd",ocount)