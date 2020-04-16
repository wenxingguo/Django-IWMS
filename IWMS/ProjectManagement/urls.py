from django.urls import path
from . import views 

app_name='ProjectManagement'

urlpatterns = [
    path('history/<str:MODEL>/', views.history_view, name='history_view'),
    path('ajax_server', views.ajax_server, name='ajax_server'),
    path('real_time/<str:MODEL>', views.real_time_view, name='real_time'),
]
