# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-28 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdpr', '0005_anon_2_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalreason',
            name='source_object_id',
            field=models.TextField(db_index=True, verbose_name='source object ID'),
        ),
        migrations.AlterField(
            model_name='legalreasonrelatedobject',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='related object ID'),
        ),
    ]
