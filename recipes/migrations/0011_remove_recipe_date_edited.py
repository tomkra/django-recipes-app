# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20151205_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='date_edited',
        ),
    ]
