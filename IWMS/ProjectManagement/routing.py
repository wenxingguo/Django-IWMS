from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/real_time/', consumers.RealTimeConsumer, name='real_time'),
    path('ws/PoolImg/', consumers.PoolIMGConsumer, name='PoolImg')

]