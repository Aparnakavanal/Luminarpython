#num=123
#digit=num%10
#=123%10
#=3
#num=num//10
#=12.33
#=12



num=int(input("enter num:"))
while(num!=0):
    digit=num%10
    print(digit,end="")
    num=num//10
