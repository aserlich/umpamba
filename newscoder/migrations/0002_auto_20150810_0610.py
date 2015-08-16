# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.CharField(blank=True, null=True, max_length=2000),
            preserve_default=True,
        ),
    ]
