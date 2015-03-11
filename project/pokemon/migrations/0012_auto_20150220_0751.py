# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_auto_20150220_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='description',
            field=models.CharField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='move',
            name='description',
            field=models.CharField(max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
    ]
