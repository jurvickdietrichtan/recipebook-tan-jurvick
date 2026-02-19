from django.urls import path
from .views import index, RecipeDetailView, recipe_detail, RecipeListView, recipe_list

urlpatterns = [
    path('recipes/list', RecipeListView.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.recipe_detail, name='recipe_detail'),
]
