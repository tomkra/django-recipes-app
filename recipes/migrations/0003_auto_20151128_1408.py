# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20151128_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.CharField(max_length=30),
        ),
    ]
