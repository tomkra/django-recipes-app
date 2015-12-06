# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20151128_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
