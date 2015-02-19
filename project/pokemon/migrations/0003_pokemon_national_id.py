# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20150219_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='national_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
