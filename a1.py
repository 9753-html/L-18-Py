from datetime import date, time, datetime
today = date.today()
print("Date=", today)
print("date components-", today.day ,"/", today.month,"/", today.year)

time=datetime.now()
print("Time=",time)