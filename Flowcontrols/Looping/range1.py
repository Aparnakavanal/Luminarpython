num=int(input("enter number:"))
low_limit=int(input("enter lower limit:"))
upper_limit=int(input("enter upper limit:"))
for i in range(1,upper_limit+1):
    if i**num in range(low_limit,upper_limit+1):
        print(i**num)
