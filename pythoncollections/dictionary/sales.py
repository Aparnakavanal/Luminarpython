expens={"jan":28000,"feb":30000,"march":40000,"april":38000,"may":35000}

print(expens)
print(expens["feb"])

expens["april"]-=2000  #update
print(expens)

expens["june"]=45000  #add new
print(expens)

# for "march" in expens:
#     print("entrt"
#           "y exist")
# else:
#     print("not exist")


for k in expens:
    print(k)