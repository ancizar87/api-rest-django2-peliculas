from .models import Pelicula, PeliculaFavorita
from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pelicula
    # fields = ['id', 'genero', 'director', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
  
  pelicula = PeliculaSerializer()

  class Meta:
    model = PeliculaFavorita
    fields = ['pelicula']
    