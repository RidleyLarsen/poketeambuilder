from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from .views import PokemonViewset, TypeViewset

router = routers.DefaultRouter()
router.register(r'pokemon', PokemonViewset)
router.register(r'type', TypeViewset)

urlpatterns = patterns(
    'pokemon.views',
    url(r'^', include(router.urls)),
)
