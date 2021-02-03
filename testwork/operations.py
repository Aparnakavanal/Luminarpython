
import functions.MyMathModule
addres=functions.MyMathModule.add(100,200)
print(addres)



from functions.MyMathModule import *
addres=add(10,20)
subres=sub(50,10)

import functions.MyMathModule as mp
addres=mp.add(10,20)