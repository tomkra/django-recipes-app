# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20151128_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.CharField(max_length=1, choices=[('B', 'Beginner'), ('A', 'Advanced'), ('E', 'Expert'), ('M', 'Magical')]),
        ),
    ]
