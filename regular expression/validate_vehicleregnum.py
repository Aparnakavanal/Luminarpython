from re import *
rule="KL[0-9]{2}[A-Z]{2}[0-9]{1,4}"   # "KL/d{2}[A-Z]{2}/d{1,4}"
variablename=input("enter variable name")

matcher=fullmatch(rule,variablename)
if matcher!=None:
    print("valid variable name")
else:
    print("invalid variable name")