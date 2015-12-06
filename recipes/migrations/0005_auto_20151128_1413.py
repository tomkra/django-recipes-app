# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20151128_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=10)),
                ('c_title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=1000)),
                ('date_commented', models.DateTimeField()),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='coment',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Coment',
        ),
    ]
