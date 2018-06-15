from django.shortcuts import render
from . import views
from api.models import Recipe, Ingridient
from rest_framework import viewsets
from api.serializers import RecipeSerializer, IngridientSerializer

# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngridientViewSet(viewsets.ModelViewSet):
    
    queryset = Ingridient.objects.all()
    serializer_class = IngridientSerializer