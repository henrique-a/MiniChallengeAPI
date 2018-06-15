from rest_framework import serializers, status
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

    def create(self, validated_data):
        
        ingridient_data = validated_data.pop('ingridient')
        ingridient = IngridientSerializer.create(IngridientSerializer(), validated_data=ingridient_data)
        recipe, created = Recipe.objects.update_or_create(name=validated_data.pop('name'),
                            howToPrepare=validated_data.pop('howToPrepare'),
                            timeToPrepare=validated_data.pop('timeToPrepare'),
                            portions=validated_data.pop('portions'),
                            ingridient=ingridient)
        return recipe