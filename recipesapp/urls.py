from django.urls import path
from .views import RecipeListCreate, RandomListCreate

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('random/', RandomListCreate.as_view(), name='random-list-create'),
]
