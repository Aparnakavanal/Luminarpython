arr=[10,11,12,13,14,15,16]
element=int(input("enter element for search:"))
#arr.sort()
low=0
upp=len(arr)-1
flg=0

while(low<=upp):
    mid=(low+upp)//2
    if(element>arr[mid]):
        low=mid+1
    elif(element<arr[mid]):
        upp=mid-1
    elif(element==arr[mid]):
        flg=1
        break

if(flg==0):
    print("element not found")
else:
    print("found")
