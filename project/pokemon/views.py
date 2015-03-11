from django.views.generic import ListView
from rest_framework import viewsets

from .models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer


class PokemonListView(ListView):
    model = Pokemon

    class Meta:
        ordering = ('national_id',)


class PokemonViewset(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.filter(national_id__lte=900).order_by('national_id')

    class Meta:
        model = Pokemon


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
