n = int(input())
add = []
for i in range(n+1):
    if(i%12==0):
        add.append(i)
non = (str(xo) for xo in add)
res = ", ".join(non)
print(res)
