# n = int(input())
# add=[]
# for i in range(n+1):
#     if(i%2==0):
#         add.append(i)
# buka = (str(x) for x in add)
# res = ", ".join(buka)
# print(res)
       
def opa(n):
    for i in range(n+1):
        if(i%2==0):
            yield(i)

n = int(input())
add=[]
for i in opa(n):
    add.append(i)
buka = (str(x) for x in add)
res = ", ".join(buka)
print(res)

