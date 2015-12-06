# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(verbose_name=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(120)])),
                ('experience', models.CharField(max_length=1, choices=[(b'B', b'Beginner'), (b'A', b'Advanced'), (b'E', b'Expert'), (b'M', b'Magical')])),
                ('date_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=10)),
                ('c_title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=1000)),
                ('date_commented', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r_title', models.CharField(max_length=70)),
                ('ingredients', models.CharField(max_length=255)),
                ('process', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('date_edited', models.DateTimeField()),
                ('chef', models.ForeignKey(to='recipes.Chef')),
            ],
        ),
        migrations.AddField(
            model_name='coment',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
    ]
