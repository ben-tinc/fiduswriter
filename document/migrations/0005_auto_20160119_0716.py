# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 13:16


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_auto_20160104_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='contents',
            field=models.TextField(default='{"nn":"DIV","a":[],"c":[{"nn":"P","c":[]}]}'),
        ),
    ]
