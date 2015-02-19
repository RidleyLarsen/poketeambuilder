# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='abilities',
            field=models.ManyToManyField(to='pokemon.Ability', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='pokemon.Move', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(to='pokemon.Type', null=True, blank=True),
            preserve_default=True,
        ),
    ]
