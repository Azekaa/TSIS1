def lol(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

str = input()
print(lol(str))