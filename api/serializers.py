from rest_framework import serializers
from api.models import Recipe
from api.models import Ingridient


class IngridientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingridient
        fields = '__all__'

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'