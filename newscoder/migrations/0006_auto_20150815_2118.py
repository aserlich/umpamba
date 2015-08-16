# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0005_auto_20150815_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storycoding',
            old_name='story_id',
            new_name='story',
        ),
    ]
