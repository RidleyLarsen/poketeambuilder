from django.views.generic import ListView
from django.core.cache import cache
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .models import Pokemon, Type
from .serializers import BasicPokemonSerializer, TypeSerializer


class PokemonListView(ListView):
    model = Pokemon

    class Meta:
        ordering = ('national_id',)


class PokemonViewset(viewsets.ModelViewSet):
    serializer_class = BasicPokemonSerializer
    queryset = Pokemon.objects.filter(national_id__lte=900).order_by('national_id')

    def list(self, request):
        allpkmn = cache.get('allpkmn')
        if not allpkmn:
            allpkmn = Pokemon.objects.filter(national_id__lte=900).order_by('national_id')
            pkmn_serializer = BasicPokemonSerializer(allpkmn, many=True)
            json_data = JSONRenderer().render(pkmn_serializer.data)
            cache.set('allpkmn', json_data)
        return JsonResponse(allpkmn)

    class Meta:
        model = Pokemon


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
