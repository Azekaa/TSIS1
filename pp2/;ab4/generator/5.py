# n = int(input())
# for i in range(n,-1,-1):
#     print(i)
def opa(n):
    for i in range(n,-1.-1):
      yield(i)
n = int(input())
for i in opa(n):
   print(i)
