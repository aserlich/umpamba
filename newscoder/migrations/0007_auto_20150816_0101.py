# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0006_auto_20150815_2118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coder',
        ),
        migrations.AddField(
            model_name='storycoding',
            name='coder_id',
            field=models.CharField(default='ezra', max_length=100),
            preserve_default=False,
        ),
    ]
