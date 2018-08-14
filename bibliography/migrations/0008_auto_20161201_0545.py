# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 11:45


from tornado.escape import json_decode, json_encode
from django.db import migrations


def modify_fields(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Entry = apps.get_model("bibliography", "Entry")
    for entry in Entry.objects.all():
        fields = json_decode(entry.fields)
        # If the entry has no title, add an empty title
        if not "title" in fields:
            fields["title"] = []
        # If the entry has no date, add an uncertain date
        if not "date" in fields:
            fields["date"] = 'uuuu'
        # If the entry has no author or editor, add an empty author
        if not "author" in fields and not "editor" in fields:
            fields["author"] = [{'literal': []}]
        entry.fields = json_encode(fields)
        entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0007_auto_20161201_0209'),
    ]

    operations = [
        migrations.RunPython(modify_fields),
    ]
