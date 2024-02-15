import datetime
t = datetime.datetime(2024,3,5,6,5,4)
v = datetime.datetime(2030,5,3,6,7,8)
raz = abs(t-v)
sec = raz.total_seconds()
print(int(sec))