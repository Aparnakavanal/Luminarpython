

from re import *

rule="KL[0-9]{2}[A-Z]{2}[0-9]{1,4}"
f=open("vehicleregnum","r")
for lines in f:
    # print(lines)
    matcher=fullmatch(rule,lines)
    if matcher != None:
        print("valid variable name")
    else:
        print("invalid variable name")