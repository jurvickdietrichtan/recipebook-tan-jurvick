from django.urls import path
from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', recipe_detail, name='recipe_detail'),
]


#from .views import index, RecipeDetailView, recipe_detail, RecipeListView, recipe_list

#urlpatterns = [
#    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
#    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
#]
