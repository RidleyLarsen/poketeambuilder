# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_auto_20150219_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='growth_rate',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
