# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='likes',
            new_name='views',
        ),
    ]