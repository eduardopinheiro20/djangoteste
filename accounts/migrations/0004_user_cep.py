# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-13 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180506_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cep',
            field=models.CharField(blank=True, max_length=11, verbose_name='CEP'),
        ),
    ]
