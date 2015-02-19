from django.contrib import admin

from .models import Ability, Type, Move, EggGroup, Description, Sprite, Game, Pokemon

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Ability)
admin.site.register(Type)
admin.site.register(Move)
admin.site.register(EggGroup)
admin.site.register(Description)
admin.site.register(Sprite)
admin.site.register(Game)