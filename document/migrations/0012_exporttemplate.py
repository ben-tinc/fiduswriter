# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 22:50


from django.db import migrations, models
import document.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0011_auto_20160515_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, default='', max_length=255)),
                ('file_type', models.CharField(choices=[('docx', 'Docx'), ('odt', 'ODT')], max_length=5)),
                ('template_file', models.FileField(upload_to=document.models.template_filename)),
            ],
        ),
    ]
