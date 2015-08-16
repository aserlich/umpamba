# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscoder', '0003_auto_20150810_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='summary',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
