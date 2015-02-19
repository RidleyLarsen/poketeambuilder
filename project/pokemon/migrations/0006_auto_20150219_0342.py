# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_auto_20150219_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='ev_yield',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
