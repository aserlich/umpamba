# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0002_auto_20150810_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='story_text',
        ),
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.CharField(default='', max_length=2000, blank=True),
            preserve_default=True,
        ),
    ]
