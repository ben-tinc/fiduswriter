# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 07:30


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0008_auto_20161201_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_cat',
            field=models.TextField(default='[]'),
        ),
    ]
