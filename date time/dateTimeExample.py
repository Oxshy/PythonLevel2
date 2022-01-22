# import datetime as d
# Y=d.date(2022,1,15)
# print(Y.year)
# print(Y.strftime("%d/%m/%y"))
# print(d.date.today())
# from datetime import time
# t=time(11,18,52)
# print(t.hour)
# print(t.strftime("%M %H %S"))
from datetime import datetime, timedelta
print(datetime.now())
dt=datetime(2022,1,15,3,34,32,24)
dtA=dt-timedelta(days=3)
print(dtA.strftime("%d"))