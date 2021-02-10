arr=[1,2,3,4]
num=6

low=0
upp=len(arr)-1
while(low<upp):
    total=arr[low]+arr[upp]
    if num==total:
        print(arr[low],arr[upp])
        low+=1
        upp-=1
        break
    elif total>num:
        upp-=1

    elif total<num:
        low+=1

