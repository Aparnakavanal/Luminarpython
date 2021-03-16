lst=[10,20,30]
pos=int(input("enter position"))

try:
    print(lst[pos])
except Exception as e:
    print(e.args)
