# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='secret',
            name='liked_by',
            field=models.ManyToManyField(related_name='has_liked_secrets', to='dashboard.User'),
        ),
    ]
