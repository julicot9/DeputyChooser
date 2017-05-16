# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vote, Question, Category, User

# Register your models here.

admin.site.register(Vote)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(User)