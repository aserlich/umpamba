# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0007_auto_20150816_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='selected',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
