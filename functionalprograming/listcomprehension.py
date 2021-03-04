lst1=[1,2,3]
lst2=[3,4,5]
op=[(i,j)for i in lst1 for j in lst2]
print(op)

sq=[i**2 for i in lst1]
print(sq)

n=[i for i in lst1 if i%2==0]
print(n)

cmn=[(i,j)for i in lst1 for j in lst2 if i==j]
print(cmn)




lst=[3,4,2,6,7,8]
n=[i-1 if i<5 else i+1 for i in lst]
print(n)
