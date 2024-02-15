def Squares(N):
    for i in range(N+1):
        yield i**2
lim = int(input())

for i in Squares(lim):
    print(i)

