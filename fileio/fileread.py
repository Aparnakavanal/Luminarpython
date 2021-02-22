f=open("demo","r")
lst=[]
for lines in f:
    print(lines)
    lst.append(lines.rstrip("\n"))

print(lst)



f=open("demo","r")
lst=[]
#st=set(st)
for lines in f:

    lst.append(lines.rstrip("\n"))
    st=set(lst)

print(st)