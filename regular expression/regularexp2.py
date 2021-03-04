from re import *

# pattern='[ab]'   #either a or b
# pattern='[a-z]'   #checking for lower case alphabets
# pattern='[A-Z]'    #upper case
# pattern='[a-zA-Z]'
# pattern='[0-9]'      #checking for digits
# pattern="[a-zA-z0-9]"
# pattern='[^0-9]'    #except digits
# pattern="[^a-zA-z0-9]"
# pattern="\s"      #space
# pattern="\d"      #digits
# pattern="\D"      #^0-9
# pattern="\w"      #all words
pattern="\W"





source="ab Z@c2a"

matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())

print("count",cnt)