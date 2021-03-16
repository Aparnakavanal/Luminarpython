no1=int(input("enter no1"))
no2=int(input("enter no2"))
try:
    res=no1/no2
    print(res)
# except Exception as e:
#     print(e.args)   #print type of exception

except Exception as e:
    no2 = int(input("enter no2"))
    try:
        res=no1/no2
        print(res)
    except Exception as e:
        print(e.args)

finally:
    print("database operation")
    print("file write")










