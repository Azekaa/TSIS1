n= input()
b=[]
n = n.split()
n.reverse()
print(" ".join(n))

def reversed(str):
    words = str.split()
    words.reverse()
    strRev = ""
    for word in words:
        strRev = strRev + word + " "
    print (strRev)

str = input()
reversed(str)