import datetime, time
import random
#from django.utils import timezone
from ProjectManagement.models import Station, Voltage,Current,Sound

#print(Station.objects.all())
time_stamp = int(datetime.datetime.now().timestamp())#当前时间戳
one_day = 24*3600
i = 0
#Station(name='station 2', description='This is Station 2').save()
station_ = Station.objects.get(pk=1)
print(station_.name)
while i < one_day:
    v = Voltage(Station=station_, date_time= int(datetime.datetime.now().timestamp()), value = 120+(random.random()-0.5)*20)
    v.save()
    i += 5
    time.sleep(2);


#print(time_stamp)