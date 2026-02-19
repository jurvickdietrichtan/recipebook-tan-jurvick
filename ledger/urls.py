from django.urls import path
from .views import index, RecipeDetailView, recipe_detail, RecipeListView, recipe_list

urlpatterns = [
    path('recipes/list', RecipeListView.as_view, name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view, name='recipe_detail'),
]
