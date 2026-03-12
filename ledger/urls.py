from django.urls import path
from django.urls import path
from . import views
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
    path("recipe/add/", views.RecipeCreateView.as_view(), name="recipe_add"),
    path("recipe/<int:pk>/add_image/", views.RecipeImageCreateView.as_view(), name="add_image"),
    ]


