#num=int(input("enter number:"))
#flg=0
#for i in range(20,50):
  #  if(num>=20)&(num<=50):
 #       flg=1
 #       break
  #  else:
   #     flg=0
#if(flg==1):
 #   print("true")
## print("false")

num=int(input("enter number:"))
if num in range(20,50):
    print("true")
else:
    print("false")