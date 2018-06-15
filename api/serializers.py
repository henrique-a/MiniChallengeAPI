from rest_framework import serializers, status
from api.models import Recipe
from api.models import Ingridient


class IngridientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.RelatedField(source='recipe')

    class Meta:
        model = Ingridient
        fields = '__all__'

    # def create(self, validated_data):
    
    #     recipe_data = validated_data.pop('recipe')
    #     recipe = RecipeSerializer.create(RecipeSerializer(), validated_data=recipe_data)
    #     ingridient, created = Ingridient.objects.update_or_create(description=validated_data.pop('description'),
    #                         quantity=validated_data.pop('quantity'),
    #                         unity=validated_data.pop('unity'),
    #                         recipe=recipe)
    #     return recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    