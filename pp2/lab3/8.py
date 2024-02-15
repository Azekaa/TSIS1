n=int(input())
arr=[]
abb=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
for j in range(0,n):
    if(arr[j]==0):
        abb.append(arr[j])
    if(arr[j]==7):
        abb.append(arr[j])
if(abb[0]==0 and abb[1]==0 and abb[2]==7):
    print("TRUE")
else:
    print("FAlSE")



def spy(arr):
    arr=[]
    abb=[]
    for j in range(0,len(arr)-1):
        if(arr[j]==0):
            abb.append(arr[j])
        if(arr[j]==7):
             abb.append(arr[j])
    if(abb[0]==0 and abb[1]==0 and abb[2]==7):
        print("TRUE")
    else:
        print("FAlSE")


numbers = list(map(int, input().split()))

print(spy(numbers))