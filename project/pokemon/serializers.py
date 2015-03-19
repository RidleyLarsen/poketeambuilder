from rest_framework import serializers

from .models import Pokemon, Type, Ability, Move


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name', 'ineffective_types',)


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('id', 'name', 'description', )


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'name', 'description', )


class BasicPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            'name',
            'types',
            # 'sprite_img',
            'national_id',
        )


class PokemonSerializer(serializers.ModelSerializer):
    # types = TypeSerializer()
    # moves = MoveSerializer()
    # abilities = AbilitySerializer()

    class Meta:
        model = Pokemon
        fields = (
            'name',
            'catch_rate',
            'species',
            'types',
            'moves',
            'abilities',
            'hp',
            'attack',
            'defense',
            'sp_atk',
            'sp_def',
            'speed',
            'attr_total',
            'egg_cycles',
            'ev_yield',
            'exp',
            'growth_rate',
            'male_female_ratio',
            'happiness',
            'height',
            'weight',
            'national_id',
            'sprite_img',
        )
