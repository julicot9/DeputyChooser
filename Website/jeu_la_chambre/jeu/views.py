# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_list_or_404, get_object_or_404
from models import Category, Question, Vote, User, ScoreDep, AnswQuest
from django.http.response import HttpResponseRedirect
from bulkops import update_many

def categoryV(request): 

    CookUser=request.COOKIES['username']
    ID=get_object_or_404(User,username=CookUser)

    
    if ID.langue=="nl":
        pair=range(0,10000,2)
    elif ID.langue=="fr":
        pair=range(1,10000,2)
    
    questions=Question.objects.filter(pk__in=pair)
    
    frcatID=[]
    for question in questions:
        frcatID.append(question.category_id)

        

    all_category=Category.objects.filter(id__in=frcatID)

    
    context={'all_category': all_category,
             }
    
    return render(request, 'category.html', context)

def questionV(request,category_id):
    
    
    
    CookUser=request.COOKIES['username']
    ID=get_object_or_404(User,username=CookUser)
    answQuestions=AnswQuest.objects.filter(user_id=ID.id)
    
    
    if ID.langue=="nl":
        pair=range(0,100000,2)
    elif ID.langue=="fr":
        pair=range(1,100000,2)
    
    questions=Question.objects.filter(category=category_id,pk__in=pair)
    
    """
    for question in questions:
        if ID.langue=="nl" and i%2==0:
            questions=questions.exclude(pk=question.id)
        elif ID.langue=="fr" and i%2==1:
            questions=questions.exclude(pk=question.id)
        i=i+1
   """
    """
    for questlang in questions:
        if ID.langue=="nl" and questlang.id%2==1:
            questions=questions.exclude(pk=questlang.id)
        elif ID.langue=="fr" and questlang.id%2==0:
            questions=questions.exclude(pk=questlang.id)
"""
    
    for quest in answQuestions:
        questions=questions.exclude(pk=quest.question_id)
        
    category=Category.objects.filter(id=category_id)[0].category
    context={
             'all_questions': questions,
             'this_category': category,
             }
    return render(request,'questions.html',context)
    
    
def verdict(request):
    CookUser=request.COOKIES['username']
    ID=get_object_or_404(User,username=CookUser)
    
    answers=get_list_or_404(AnswQuest,user_id=ID.id)
    scoresD=get_list_or_404(ScoreDep,user_id=ID.id)
    
    listQuest=[]
    listScores=[]
    listDepute=[]
    listScoreSort=[]
    
    for answer in answers:
        question=Question.objects.get(pk=answer.question_id)
        listQuest.append(question.question+"\n"+answer.answer)
        
        
    
    for scores in scoresD:
        listDepute.append(scores.name)
        listScoreSort.append(scores.score)
    
    listScoreSort, listDepute = (list(t) for t in zip(*sorted(zip(listScoreSort, listDepute))))
    listScoreSort=listScoreSort[::-1]
    listDepute=listDepute[::-1]
    
    
    i=0
    for score in listScoreSort:
        listScores.append(listDepute[i]+" "+str(score))
        i=i+1
        
    

    context={
             'questions': listQuest,
             'scores': listScores,
             }
    
    return render(request,'verdict.html',context)


def soumettre(request, question_id):
    votes=get_list_or_404(Vote,question_id=question_id)
    voteUtil=request.POST['voteUtil']
    
    CookUser=request.COOKIES['username']
    ID=get_object_or_404(User,username=CookUser)
    
    scores=get_list_or_404(ScoreDep,user_id=ID.id)
    i=0
    
    questA=get_object_or_404(Question,id=question_id)
    
    userA=get_object_or_404(User,id=ID.id)
    
    answ=AnswQuest(question=questA,user=userA,answer=voteUtil)
    answ.save()
    
    for vote in votes:
        if((voteUtil=="Oui" and vote.vote=="1") or (voteUtil=="Non"and vote.vote=="-1") or (voteUtil=="Abstention"and vote.vote=="2")):
            scores[i].score=scores[i].score+1
            
        
        elif((voteUtil=="Oui"and vote.vote=="-1") or (voteUtil=="Non" and vote.vote=="1")):
            scores[i].score=scores[i].score-1
            
        
        i=i+1
    update_many(scores)
    
    
    return HttpResponseRedirect("/jeu/"+str(questA.category_id))
