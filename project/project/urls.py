from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from pokemon.views import PokemonListView
from .views import HomepageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pkmn/', PokemonListView.as_view(), name="pokemon"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^pokemon/', include('pokemon.urls', namespace="pokemon")),
)

if settings.DEBUG:
    # This is not suitable for production use!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)