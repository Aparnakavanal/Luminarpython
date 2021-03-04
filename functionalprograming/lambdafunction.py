add=lambda num1,num2:num1+num2
print(add(100,200))

sub=lambda num1,num2:num1-num2
print(sub(200,100))

mul=lambda num1,num2:num1*num2
print(mul(100,200))

cube=lambda num1:num1**3
print(cube(100))

div=lambda num1,num2:num1/num2
print(div(100,200))


#map(arg1,arg2)
lst=[1,2,3,4,5]
sq=list(map(lambda num1:num1**2,lst))
print(sq)

names=["ram","raju","ravi"]
up=list(map(lambda name:name.upper(),names))
print(up)

#filter
lst=[1,2,3,4,5]
evn=list(filter(lambda num:num%2==0,lst))
print(evn)

grtr=list(filter(lambda num:num>2,lst))
print(grtr)