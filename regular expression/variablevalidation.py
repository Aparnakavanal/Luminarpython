# q: *first character must be an alphabet, second character must be a digit divisible by 3,
# followed by any no.of characters


from re import *
rule="[a-kA-K][369][a-zA-Z0-9]*"
variablename=input("enter variable name")

matcher=fullmatch(rule,variablename)   # fullmatch:exact match
if matcher!=None:
    print("valid variable name")
else:
    print("invalid variable name")