n=int(input("enter num:"))
flg=0
for i in range(2,n):
    if(n%i==0):
        flg=1
        break

    else:
        flg=0

if(flg==0):
    print("prime")
else:
    print("not prime")
