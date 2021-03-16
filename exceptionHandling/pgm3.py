no=int(input("enter number"))
try:
    if no<0:
        raise Exception("invalid")
except Exception as e:
    print(e.args)


