def haha(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
arr = (list(map(int, input().split())))
haha(arr)