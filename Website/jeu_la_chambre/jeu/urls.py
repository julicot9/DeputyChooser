'''
Created on 22 Apr 2017

@author: root
'''

from . import views
from django.conf.urls import url

app_name='jeu'

urlpatterns = [
    url(r'^$',views.categoryV, name='URLjeu'),
    url(r'^(?P<category_id>[0-9]+)/$',views.questionV,name='URLquestions'),
    
    url(r'^verdict/$',views.verdict,name='URLverdict'),
    
    url(r'^(?P<question_id>[0-9]+)/soumettre/$',views.soumettre,name='soumettre'),
]