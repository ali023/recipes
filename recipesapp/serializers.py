from rest_framework import serializers
from .models import Recipe, Random

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients']

class RandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Random
        fields = ['dish', 'country']
