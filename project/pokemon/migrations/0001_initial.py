# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Ability',
                'verbose_name_plural': 'Abilities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EggGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'EggGroup',
                'verbose_name_plural': 'EggGroups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('name', models.CharField(max_length=64)),
                ('generation', models.IntegerField()),
                ('release_year', models.IntegerField()),
                ('resource_uri', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('power', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('category', models.CharField(max_length=32)),
                ('pp', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Move',
                'verbose_name_plural': 'Moves',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('catch_rate', models.IntegerField()),
                ('species', models.CharField(max_length=32)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('attr_total', models.IntegerField()),
                ('egg_cycles', models.IntegerField()),
                ('ev_yield', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('growth_rate', models.CharField(max_length=8)),
                ('male_female_ratio', models.CharField(max_length=16)),
                ('happiness', models.IntegerField()),
                ('height', models.CharField(max_length=16)),
                ('weight', models.CharField(max_length=16)),
                ('abilities', models.ManyToManyField(to='pokemon.Ability')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_pokemon', models.ForeignKey(related_name='from_pokemon', to='pokemon.Pokemon')),
                ('to_pokemon', models.ForeignKey(related_name='to_pokemon', to='pokemon.Pokemon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sprite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('image', models.URLField()),
                ('pokemon', models.ForeignKey(to='pokemon.Pokemon')),
            ],
            options={
                'verbose_name': 'Sprite',
                'verbose_name_plural': 'Sprites',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_created', models.DateTimeField()),
                ('api_modified', models.DateTimeField()),
                ('resource_uri', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation_type', models.CharField(max_length=32)),
                ('from_type', models.ForeignKey(related_name='from_type', to='pokemon.Type')),
                ('to_type', models.ForeignKey(related_name='to_type', to='pokemon.Type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='type',
            name='type_relations',
            field=models.ManyToManyField(related_name='related_to', through='pokemon.TypeRelation', to='pokemon.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='evolutions',
            field=models.ManyToManyField(to='pokemon.Pokemon', through='pokemon.PokemonEvolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='pokemon.Move'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(to='pokemon.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='egggroup',
            name='pokemon',
            field=models.ManyToManyField(to='pokemon.Pokemon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='games',
            field=models.ManyToManyField(to='pokemon.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='pokemon',
            field=models.ForeignKey(to='pokemon.Pokemon'),
            preserve_default=True,
        ),
    ]
