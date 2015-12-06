# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20151128_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='age',
            field=models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.CharField(max_length=1, choices=[(b'B', b'Beginner'), (b'A', b'Advanced'), (b'E', b'Expert'), (b'M', b'Magical')]),
        ),
    ]
