# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]