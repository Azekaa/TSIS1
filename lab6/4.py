import time,math

def opa(num,sec):
    time.sleep(sec/1000)
    pow = math.sqrt(num)
    return pow
num = int(input())
sec = int(input())
res = opa(num,sec)
print(f"Square root of {num} after {sec} miliseconds is {res}")