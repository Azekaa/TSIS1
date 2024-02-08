
n=int(input())
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
for j in range(0,n):
    if(arr[j]==3):
        if(arr[j]==arr[j+1]):
            print("TRUE")
            break
        else: 
            print("FALSE")

def ha(arr):
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1] == 3):
            return True
    return False
 
numbers = list(map(int, input().split()))

print(ha(numbers))