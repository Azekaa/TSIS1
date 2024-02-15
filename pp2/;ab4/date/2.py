import datetime
t = datetime.date.today()
to = t + datetime.timedelta(days=1)
y = t - datetime.timedelta(days=1)
print("today is:",t,"\n" "tomorow is:",to,"\n" "yesterday is:",y)