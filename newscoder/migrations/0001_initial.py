# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('coder_name', models.CharField(max_length=100)),
                ('coder_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_text', models.CharField(max_length=2000)),
                ('author', models.CharField(max_length=2000)),
                ('downloaded_at', models.CharField(max_length=2000)),
                ('_id', models.CharField(serialize=False, max_length=2000, primary_key=True)),
                ('meta_description', models.CharField(max_length=2000)),
                ('owner', models.CharField(max_length=2000)),
                ('publication', models.CharField(max_length=2000)),
                ('published', models.CharField(max_length=2000)),
                ('sub_type', models.CharField(max_length=2000)),
                ('summary', models.CharField(max_length=2000)),
                ('text', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=2000)),
                ('url', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryCoding',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('story_id', models.IntegerField(default=-10)),
                ('coder_id', models.IntegerField()),
                ('coder_coding', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
