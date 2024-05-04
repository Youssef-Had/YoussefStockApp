from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^getdata',views.getdata,name='getdata')
]