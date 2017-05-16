import csv
from jeu.models import Category, Vote, Question
with open('/home/django/Documents/workspace/PolitiqueBelge/src/root/nested/dataSQL.csv') as data:
	reader=csv.reader(data,delimiter='|', quotechar='"')
	first =0
	restart=1
	voteno=1
	for row in reader:
		if first==0:
			first=1
			firstline=row
		elif row[1]!="":
			if restart<2415:
				restart=restart+1
			elif restart==2415:
				restart=restart+1
				
				categ=Category(category=row[3],id=2418)
				categ.save()
				quest=Question(question=row[1],urlpdf=row[2],category=categ,id=2418)
				quest.save()
				for i in range(4,len(row)):
					if voteno<=77:
						voteno=voteno+1
					else:
						
						vote=Vote(name=firstline[i],vote=int(row[i]),question=quest,id=voteno+410380)
						vote.save()
						voteno=voteno+1
			else:
				categ=Category(category=row[3])
				categ.save()
				quest=Question(question=row[1],urlpdf=row[2],category=categ)
				quest.save()
			
				for i in range(4,len(row)):
					vote=Vote(name=firstline[i],vote=int(row[i]),question=quest,id=voteno+410380)
					vote.save()
					voteno=voteno+1