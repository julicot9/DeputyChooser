'''
Created on 6 May 2017

@author: root
'''

from django.conf.urls import url
from . import views


app_name='Login'

urlpatterns = [
    url(r'^$',views.homepage, name='homepage'),
    url(r'^newUser/',views.newUser,name='newUser'),
    url(r'^Login/',views.Login,name='Login'),
    ]
