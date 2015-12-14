# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_remove_recipe_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced'), ('Expert', 'Expert'), ('Magical', 'Magical')], default='Beginner', max_length=50),
        ),
    ]
