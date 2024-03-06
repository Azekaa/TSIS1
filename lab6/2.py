str = input()

Upper = sum(map(lambda x: x.isupper(), str))
Lower = sum(map(lambda x: x.islower(), str))
print(Upper , Lower)
