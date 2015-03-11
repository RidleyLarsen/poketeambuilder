import urllib
import json

from pprint import pprint
from pokemon.models import Pokemon, Type, TypeRelation, Ability, Game, Move, Description, EggGroup, PokemonEvolution, Sprite
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_all_sprites()


def convert_uri_to_url(uri):
    return "http://pokeapi.co/" + uri


def prep_api_for_db(data, _class):
    data['api_created'] = data.pop('created')
    data['api_modified'] = data.pop('modified')
    try:
        data.pop('id')
    except KeyError:
        pass
    obj, created = _class.objects.get_or_create(name=data['name'])
    for attr, value in data.iteritems():
        try:
            setattr(obj, attr, value)
        except:
            print "bad attr", attr
    obj.save()
    return obj


def create_ability_from_api(data):
    base_ability, data = prep_api_for_db(data, Ability)
    for attr, value in data.iteritems():
        setattr(base_ability, attr, value)
    base_ability.save()
    return base_ability


def create_move_from_api(data):
    base_move, data = prep_api_for_db(data, Move)
    for attr, value in data.iteritems():
        setattr(base_move, attr, value)
    base_move.save()
    return base_move


def create_evolutions_from_api(data):
    base_evolution, data = prep_api_for_db(data, PokemonEvolution)
    for attr, value in data.iteritems():
        setattr(base_evolution, attr, value)
    base_evolution.save()
    return base_evolution


def create_description_from_api(data):
    base_description, data = prep_api_for_db(data, Description)
    for attr, value in data.iteritems():
        setattr(base_description, attr, value)
    base_description.save()
    return base_description


def create_egg_group_from_api(data):
    base_egg_group, data = prep_api_for_db(data, EggGroup)
    for attr, value in data.iteritems():
        setattr(base_egg_group, attr, value)
    base_egg_group.save()
    return base_egg_group


def create_sprite_from_api(data):
    base_sprite, data = prep_api_for_db(data, Sprite)
    for attr, value in data.iteritems():
        if attr == "pokemon":
            setattr(base_sprite, "pokemon", Pokemon.objects.get(name=value['name'].title()))
        else:
            setattr(base_sprite, attr, value)
    base_sprite.save()
    return base_sprite


def create_pkmn_from_api(data):
    abilities = data.pop('abilities')
    moves = data.pop('moves')
    types = data.pop('types')
    descriptions = data.pop('descriptions')
    evolutions = data.pop('evolutions')
    egg_groups = data.pop('egg_groups')
    sprites = data.pop('sprites')

    data.pop("pkdx_id")
    data['attr_total'] = data.pop('total')
    data['api_created'] = data.pop('created')
    data['api_modified'] = data.pop('modified')

    if not data['ev_yield']:
        data['ev_yield'] = 0

    pokemon, created = Pokemon.objects.get_or_create(**data)

    for a in abilities:
        _ability = Ability.objects.get(name__iexact=a['name'].title())
        pokemon.abilities.add(_ability)
    for m in moves:
        _move = Move.objects.get(name__iexact=m['name'].title())
        pokemon.moves.add(_move)
    for t in types:
        _type = Type.objects.get(name__iexact=t['name'].title())
        pokemon.types.add(_type)
    # for e in evolutions:
    #     print "Adding evolutions: ", e['name']
    #     _evolution = create_evolutions_from_api(d)
    #     pokemon.evolutions.add(_evolution)
    for egg in egg_groups:
        _egg_group = EggGroup.objects.get(name__iexact=egg['name'].title())
        _egg_group.pokemon.add(pokemon)

    return pokemon


def get_all_games():
    url = "http://pokeapi.co/api/v1/game/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, Game)
        print "Loaded Game:", obj.name
        i += 1


def get_all_egg_groups():
    url = "http://pokeapi.co/api/v1/egg/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, EggGroup)
        print "Loaded Egg Group:", obj.name
        i += 1


def get_all_abilities():
    url = "http://pokeapi.co/api/v1/ability/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, Ability)
        print "Loaded Ability:", obj.name
        i += 1

def get_all_moves():
    url = "http://pokeapi.co/api/v1/move/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, Move)
        print "Loaded Move:", obj.name
        i += 1


def get_types():
    url = "http://pokeapi.co/api/v1/type/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, Type)
        print "Loaded Type:", obj.name
        i += 1


def set_type_relations():
    url = "http://pokeapi.co/api/v1/type/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        base_type = Type.objects.get(name=data['name'].title())

        for type_ in data.pop('ineffective'):
            if type_['name'].title() != base_type.name:
                _type, created = Type.objects.get_or_create(name=type_['name'].title())
                tr, created = TypeRelation.objects.get_or_create(from_type=base_type, to_type=_type, relation_type="ineffective")
        for type_ in data.pop('no_effect'):
            if type_['name'].title() != base_type.name:
                _type, created = Type.objects.get_or_create(name=type_['name'].title())
                tr, created = TypeRelation.objects.get_or_create(from_type=base_type, to_type=_type, relation_type="no_effect")
        for type_ in data.pop('resistance'):
            if type_['name'].title() != base_type.name:
                _type, created = Type.objects.get_or_create(name=type_['name'].title())
                tr, created = TypeRelation.objects.get_or_create(from_type=base_type, to_type=_type, relation_type="resistance")
        for type_ in data.pop('super_effective'):
            if type_['name'].title() != base_type.name:
                _type, created = Type.objects.get_or_create(name=type_['name'].title())
                tr, created = TypeRelation.objects.get_or_create(from_type=base_type, to_type=_type, relation_type="super_effective")
        for type_ in data.pop('weakness'):
            if type_['name'].title() != base_type.name:
                _type, created = Type.objects.get_or_create(name=type_['name'].title())
                tr, created = TypeRelation.objects.get_or_create(from_type=base_type, to_type=_type, relation_type="weakness")
        try:
            data.pop('id')
        except:
            pass

        print "Set Type Relation:", base_type.name
        i += 1


def get_all_types():
    get_types()
    set_type_relations()


def get_all_sprites():
    url = "http://pokeapi.co/api/v1/sprite/"
    i = 1
    while True:
        data = urllib.urlopen(url + str(i) + "/").read()
        if data == "":
            break
        else:
            data = json.loads(data)
        obj = prep_api_for_db(data, Sprite)
        obj.pokemon = Pokemon.objects.get(name__iexact=data['pokemon']['name'].title())
        obj.name = obj.name.split('_')[0]
        obj.save()
        print "Loaded Sprite:", obj.name
        i += 1



def fill_from_pokedex():
    print "Loading Data from http://pokeapi.co/"
    url = "http://pokeapi.co/api/v1/pokedex/1/"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    for pokemon in data.get('pokemon'):
        print "Saving Pokemon:", pokemon['name']
        get_pokemon(pokemon['name'], pokemon['resource_uri'])
    # get_pokemon("ivysaur", "api/v1/pokemon/2/")


def get_pokemon(name, uri):
    url = convert_uri_to_url(uri)
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    pkmn = create_pkmn_from_api(data)
    pkmn.save()
