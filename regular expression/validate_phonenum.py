from re import *
rule="91\d{10}"
variablename=input("enter variable name")

matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid variable name")