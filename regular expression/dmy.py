from re import *

rule="\d{2}-\d{2}-\d{4}"
date=input("enter date")
matcher=fullmatch(rule,date)
if matcher!=None:
    print("valid")
else:
    print("invalid")