ourList = list(map(int, list(input().split())))
num = 1
for i in ourList:
    num*=i
print(num)