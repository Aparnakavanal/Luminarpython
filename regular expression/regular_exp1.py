from re import *

pattern="ab"
source="abababbab"

matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print("count",cnt)