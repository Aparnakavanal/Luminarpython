lst=[1,2,3,4]
no=int(input("enter number"))#6
st=set(lst)

for num in st:#1,2
    op=no-num#6-1,6-2
    if op in st:
        print(num,op)
        break


#multuple pair
lst=[1,2,3,4,5,6]
no=int(input("enter number"))
st=set(lst)
out=set()

for num in st:
    op=no-num
    if (op in st)&(op!=num):
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))

print(out)
