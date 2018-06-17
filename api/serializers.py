from rest_framework import serializers, status
from api.models import Recipe
from api.models import Ingridient


class IngridientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingridient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingridients = IngridientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingridients_data = validated_data.pop('ingridients')
        recipe = Recipe.objects.create(**validated_data)
        for ingridient_data in ingridients_data:
            Ingridient.objects.create(recipe=recipe, **ingridient_data)
        return recipe