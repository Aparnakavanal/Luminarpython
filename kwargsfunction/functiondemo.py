def add(*args):# tuple format
    total=0
    for num in args:
        total+=num
    print(total)
add(20,30,40,60,10)




def print_emp_data(**args): #dictionary
    print(args)
print_emp_data(key=100,job="kakkanad",resid="kozhikode")




def print_emp_data(**args): #dictionary
    for k,v in args.items():
        print(k,v)
print_emp_data(key=100,job="kakkanad",resid="kozhikode")

