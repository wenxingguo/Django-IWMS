#改用base64
import datetime, time
from ProjectManagement.models import Station, PoolImg
import base64
half_day = 3600*13
toal = 0
img_path = 'C:\\Users\\WOOD\\Desktop\\process-img\\imgs'
station_ = Station.objects.get(pk = 1)
i = 1
#end_time_stamp = int(datetime.datetime.now().timestamp())
while toal < half_day:
    with open(img_path+"\\"+str(i)+".jpg", 'rb') as f:
        img_base64 = base64.b64encode(f.read()).decode()
        v = PoolImg(Station=station_, date_time=int(datetime.datetime.now().timestamp()), value=img_base64)
        v.save()
        print('history_poolimg/'+str(i)+'.jpg')
        i += 1
        time.sleep(0.5)