# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from jeu.models import User, Vote, ScoreDep
from bulkops import insert_many

# Create your views here.
# Create your views here.
def homepage(request):
    return render (request,'homepage.html')

def newUser(request):
    Username=request.POST['username']
    Pseudonyme=request.POST['pseudonyme']
    Langue=request.POST['langue']
    newuser=User(username=Username,pseudonyme=Pseudonyme,langue=Langue)
    newuser.save()
    response = HttpResponseRedirect("/jeu/")
    
    votes=get_list_or_404(Vote,question_id=4)
    scoreList=[]
    for vote in votes:
        scoreList.append(ScoreDep(user=newuser,score=0,name=vote.name))
    insert_many(scoreList)
    response.set_cookie('username', Username)
    
    
    
    return response


def Login(request):
    Username=request.POST['username']
    get_object_or_404(User,username=Username)
    response = HttpResponseRedirect("/jeu/")
    response.set_cookie('username', Username)
    return response


