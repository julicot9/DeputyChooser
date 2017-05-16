# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jeu', '0008_scoredep_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='answQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeu.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeu.User')),
            ],
        ),
    ]