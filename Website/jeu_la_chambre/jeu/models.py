# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.



class Category(models.Model):
    category=models.CharField(max_length=200)
    def __str__(self):
        return self.category
    
class Question(models.Model):
    question=models.CharField(max_length=2000)
    urlpdf=models.CharField(max_length=300)
    category=models.ForeignKey(Category)
    
    def __str__(self):
        return self.question
    
class Vote(models.Model):
    name=models.CharField(max_length=250)
    vote=models.CharField(max_length=2)
    question=models.ForeignKey(Question)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    username=models.CharField(max_length=250)
    pseudonyme=models.CharField(max_length=250)
    langue=models.CharField(max_length=2)
    def __str__(self):
        return self.username
    
class ScoreDep(models.Model):
    name=models.CharField(max_length=250)
    score=models.IntegerField()
    user=models.ForeignKey(User)
    def __str__(self):
        return self.score

class AnswQuest(models.Model):
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=12)
    user=models.ForeignKey(User)
    def __str__(self):
        return self.answer
    
    