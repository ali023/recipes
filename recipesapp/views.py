from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Random
from .serializers import RecipeSerializer, RandomSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Create your views here.
class RandomListCreate(generics.ListCreateAPIView):
    queryset = Random.objects.all()
    serializer_class = RandomSerializer