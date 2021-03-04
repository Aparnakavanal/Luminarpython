from re import *

# pattern="a+"    # check for one or more than a
# pattern="a*"    # a+ + zero number of a
# pattern="a{2}"   # maximum two number of a
pattern="a{2,3}"   # minimum 2, max 3

matcher=finditer(pattern,"aaacaabbaaab")
for match in matcher:
    print(match.start())
    print(match.group())
