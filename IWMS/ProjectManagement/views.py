from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from ProjectManagement.models import Voltage, Station, Current, Sound, PoolImg
import datetime, time
# Create your views here.
time_pattern = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d ",
    "%m-%d %H:%M"
]
models_dict = {
    'Station':Station,
    'Voltage':Voltage,
    'Current':Current,
    'PoolImg':PoolImg,
    'Sound':Sound
}

def history_view(request, MODEL):
    if MODEL in models_dict:
        return render(request, 'ProjectManagement/history/'+MODEL+'_history.html', {'Station_list':Station.objects.all()})
    else:
        return Http404

def ajax_server(request):
    #print(request.POST['model'])

    item_list = models_dict[request.POST['model']].objects.filter(Station__name=request.POST['station']) #筛选工位
    
    if request.POST['recent_time_range'] == "no_recent":
        start = int(time.mktime(time.strptime(request.POST['start'], time_pattern[1])))
        end = int(time.mktime(time.strptime(request.POST['end'], time_pattern[1])))

    else:
        try:
            end = item_list.last().date_time #数据库中最近的时间
        except:
            return JsonResponse({});
        if request.POST['recent_time_range'] == "one_hour":
            start = end - 3600;
        elif request.POST['recent_time_range'] == "one_day":
            start = end- 3600*24
        else:
            start = end-600

    time_data = []
    y_data = []
    item_list = item_list.filter(date_time__lte = end, date_time__gte=start)#筛选其他条件，前边的是时间早的
    
    if request.POST['model'] == 'PoolImg':
        for item in item_list:
            #y_data.append(item.value.name)
            time_data.append(item.date_time)#倒序
            #print(item.date_time)
        return JsonResponse({
            #'img_url_list':y_data,
            'timestamp_list':time_data,
            'start_time':datetime.datetime.fromtimestamp(start).strftime(time_pattern[3]),
            'end_time':datetime.datetime.fromtimestamp(end).strftime(time_pattern[3]),
        })

    
    for item in item_list:
        time_data.append(datetime.datetime.fromtimestamp(item.date_time).strftime(time_pattern[3]))#转化为固定的时间格式
        y_data.append(item.value)
    print(time_data[0]);
    return JsonResponse({
        'x':time_data,
        'y':y_data
    })


def real_time_view(request, MODEL):
    if MODEL in models_dict:
        return render(request, 'ProjectManagement/realtime/'+MODEL+'_real_time.html', {'Station_list':Station.objects.all()})


