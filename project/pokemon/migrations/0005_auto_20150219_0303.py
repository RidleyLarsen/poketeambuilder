# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_auto_20150219_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='api_created',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='type',
            name='api_modified',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
