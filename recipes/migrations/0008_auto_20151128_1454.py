# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20151128_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(110)]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.CharField(choices=[('B', 'Beginner'), ('A', 'Advanced'), ('E', 'Expert'), ('M', 'Magical')], max_length=50),
        ),
    ]
