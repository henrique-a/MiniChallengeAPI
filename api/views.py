from django.shortcuts import render
from . import views
from api.models import Recipe
from rest_framework import viewsets
from api.serializers import RecipeSerializer

# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer