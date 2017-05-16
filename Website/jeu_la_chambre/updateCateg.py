# -*- coding: utf-8 -*-
import csv
import django
django.setup()

from Login.bulkops import update_many, insert_many
from jeu.models import Category, Question



all_categ=Category.objects.all()
categList=[]
with open('/home/django/Documents/workspace/PolitiqueBelge/src/root/nested/dataSQL.csv') as data:
    reader=csv.reader(data,delimiter='_', quotechar='"')
    for row in reader:
        if row[1] != "" and row[1]!='Question':
            categ=Category.objects.filter(category=row[3])
            present=0
            for item in categList:
                if item.category==row[3]:
                    present=1
            
            if not categ and not present:
                categList.append(Category(category=row[3]))
insert_many(categList)

i=0
updateQuest=[]
with open('/home/django/Documents/workspace/PolitiqueBelge/src/root/nested/dataSQL.csv') as data:
    reader=csv.reader(data,delimiter='_', quotechar='"')
    for row in reader:
        if row[1] != "" and row[1]!='Question':
            i+=1
            print(i)
            print(row)
            a=Question.objects.get(question=row[1])
            b=Category.objects.get(category=row[3])
            a.category_id=b.id
            updateQuest.append(a)
            
update_many(updateQuest)
                