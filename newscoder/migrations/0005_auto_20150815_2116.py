# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0004_auto_20150812_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='storycoding',
            name='coder_id',
        ),
        migrations.AlterField(
            model_name='coder',
            name='coder_id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='storycoding',
            name='story_id',
            field=models.ForeignKey(to='newscoder.Story'),
            preserve_default=True,
        ),
    ]
