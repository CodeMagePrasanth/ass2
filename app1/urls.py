from django.urls import path

app_name='nothing'

from app1.views import *

urlpatterns=[
    path('index1/',index1,name='index1')
]