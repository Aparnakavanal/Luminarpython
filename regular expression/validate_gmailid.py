from re import *
rule="[a-zA-Z0-9]{1,64}@gmail.com"
variablename=input("enter variable name")

matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid")
else:
    print("invalid")