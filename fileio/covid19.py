f=open("covid_19_india(1).csv","r")
#dict={}
s={}
data1={}
for lines in f:
    data=lines.rstrip("\n").split(",")

    state=data[3]
    confirmed=int(data[-1])
    death=int(data[-2])
    cured=int(data[-3])
    data1={"s":{"state":state,"confirmed":confirmed,"death":death,"cured":cured}}
    print(data1)


