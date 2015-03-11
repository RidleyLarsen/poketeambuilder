from django.db import models

# Create your models here.


class Pokemon(models.Model):
    api_created = models.DateTimeField()
    api_modified = models.DateTimeField()
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    evolutions = models.ManyToManyField(
        'self',
        through='PokemonEvolution',
        symmetrical=False,
    )
    abilities = models.ManyToManyField('Ability', null=True, blank=True)
    moves = models.ManyToManyField('Move', null=True, blank=True)
    types = models.ManyToManyField('Type', null=True, blank=True)
    catch_rate = models.IntegerField(default=0)
    species = models.CharField(max_length=32)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    sp_atk = models.IntegerField(default=0)
    sp_def = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    attr_total = models.IntegerField(default=0)
    egg_cycles = models.IntegerField(default=0)
    ev_yield = models.CharField(max_length=32)
    exp = models.IntegerField(default=0)
    growth_rate = models.CharField(max_length=32)
    male_female_ratio = models.CharField(max_length=16)
    happiness = models.IntegerField(default=0)
    height = models.CharField(max_length=16)
    weight = models.CharField(max_length=16)
    national_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"

    def __str__(self):
        return self.name

    @property
    def sprite(self):
        return Sprite.objects.get(pokemon=self)

    @property
    def sprite_img(self):
        return self.sprite.image


class PokemonEvolution(models.Model):
    from_pokemon = models.ForeignKey(Pokemon, related_name='from_pokemon')
    to_pokemon = models.ForeignKey(Pokemon, related_name='to_pokemon')


class Ability(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Ability"
        verbose_name_plural = "Abilities"

    def __str__(self):
        return self.name


class Type(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    type_relations = models.ManyToManyField(
        'self',
        through='TypeRelation',
        symmetrical=False,
        related_name='related_to'
    )

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name

    def get_ineffective_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="ineffective"):
            types.append(tr.to_type)
        return types

    @property
    def ineffective_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="no_effect"):
            types.append(tr.to_type.id)
        return types

    def get_no_effect_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="no_effect"):
            types.append(tr.to_type)
        return types

    def get_resistance_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="resistance"):
            types.append(tr.to_type)
        return types

    def get_super_effective_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="super_effective"):
            types.append(tr.to_type)
        return types

    def get_weakness_types(self):
        types = []
        for tr in TypeRelation.objects.filter(from_type__id=self.id, relation_type="weakness"):
            types.append(tr.to_type)
        return types


class TypeRelation(models.Model):
    relation_type = models.CharField(max_length=32)
    from_type = models.ForeignKey(Type, related_name='from_type')
    to_type = models.ForeignKey(Type, related_name='to_type')


class Move(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    power = models.IntegerField(null=True, blank=True)
    accuracy = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=32, null=True, blank=True)
    pp = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Move"
        verbose_name_plural = "Moves"

    def __str__(self):
        return self.name


class EggGroup(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    pokemon = models.ManyToManyField(Pokemon)

    class Meta:
        verbose_name = "EggGroup"
        verbose_name_plural = "EggGroups"

    def __str__(self):
        return self.name


class Description(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    games = models.ManyToManyField('Game')
    pokemon = models.ForeignKey(Pokemon, null=True, blank=True)

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"

    def __str__(self):
        return self.name


class Sprite(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    pokemon = models.ForeignKey(Pokemon, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Sprite"
        verbose_name_plural = "Sprites"

    def __str__(self):
        return self.name


class Game(models.Model):
    api_created = models.DateTimeField(null=True, blank=True)
    api_modified = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=64)
    generation = models.IntegerField(null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    resource_uri = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return self.name
