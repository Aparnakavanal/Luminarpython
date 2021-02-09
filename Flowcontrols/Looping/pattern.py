# limit=int(input("enter the limit:"))
# for i in range(1,limit+1):
#     for j in range(0,i):
#         print(i,end="")
#     print("")
#
# limit=int(input("enter the limit:"))
# for i in range(1,limit+1):
#     for j in range(0,i):
#         print("*",end="")
#     print("")
#
#
# limit=int(input("enter the limit:"))
# for i in range(1,limit+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")


for r in range(1,6):

    for c in range(1,10):
       # print("",end="")
        if(r==5)|(r+c==6)|(c-r==4):
            print("*",end="")
        else:
            print("",end=" ")
    print()

