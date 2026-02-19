from django.shortcuts import render
from django.views.generic.base import TemplateView


from django.http import HttpResponse

from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def index(request):
    return HttpResponse('Sorry bro.')

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", context)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}
    return render(request, "ledger/recipe_detail.html", context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'