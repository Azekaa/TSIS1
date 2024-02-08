
def prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=[]
n=list(map(int,input().split()))
prime_list = list(filter(prime,n))
print(prime_list)

